classdef HTTPPlateLoader < handle
    % HTTPPlateLoader  Controls the plate loader through the Python Flask
    % server (HTTP) instead of a serial port.
    %
    %   robot = HTTPPlateLoader("137.112.220.248:8080");
    %
    % Each command is sent as  http://<server>/api/<COMMAND>
    % e.g.  webread("http://137.112.220.248:8080/api/X-AXIS 2")

    properties
        xAxisPosition   = 3
        isZAxisExtended = false
        isGripperClosed = true
        isPlatePresent  = false
    end
    properties (Access = private)
        BaseURL
        Options
    end
    properties (Constant = true)
        defaultTimeTable = [
            0 60 20 30 0
            0 0 30 30 0
            0 30 0 30 0
            0 30 30 0 0
            0 30 20 60 0];
    end

    methods
        function obj = HTTPPlateLoader(server)
            server = strtrim(string(server));
            if ~startsWith(server, "http")
                server = "http://" + server;
            end
            obj.BaseURL = regexprep(server, "/+$", "");
            obj.Options = weboptions('ContentType', 'text', 'Timeout', 60);
            % Same as the serial constructor, which sent INITIALIZE
            response = obj.send("INITIALIZE");
            fprintf('%s\n', response);
        end

        function response = reset(obj)
            response = obj.send("RESET");
            if startsWith(response, "ERROR"), return; end
            obj.xAxisPosition   = 3;
            obj.isZAxisExtended = false;
            obj.isGripperClosed = true;
            obj.isPlatePresent  = false;
        end

        function response = x(obj, pos)
            if pos < 1 || pos > 5
                fprintf('Illegal position\n');
                response = "ERROR: Illegal position";
                return
            end
            response = obj.send(sprintf('X-AXIS %d', pos));
            if startsWith(response, "ERROR"), return; end
            if obj.xAxisPosition ~= pos
                obj.isZAxisExtended = false;
            end
            obj.xAxisPosition = pos;
        end

        function response = extend(obj)
            response = obj.send("Z-AXIS EXTEND");
            obj.isZAxisExtended = ~startsWith(response, "ERROR");
        end

        function response = retract(obj)
            response = obj.send("Z-AXIS RETRACT");
            if startsWith(response, "ERROR"), return; end
            obj.isZAxisExtended = false;
        end

        function response = close(obj)
            response = obj.send("GRIPPER CLOSE");
            if startsWith(response, "ERROR"), return; end
            obj.isGripperClosed = true;
            obj.isPlatePresent  = ~endsWith(response, "NOPLATE");
        end

        function response = open(obj)
            response = obj.send("GRIPPER OPEN");
            if startsWith(response, "ERROR"), return; end
            obj.isGripperClosed = false;
            obj.isPlatePresent  = false;
        end

        function response = movePlate(obj, startPos, endPos)
            if startPos < 1 || startPos > 5 || endPos < 1 || endPos > 5
                fprintf('Illegal position\n');
                response = "ERROR: Illegal position";
                return
            end
            response = obj.send(sprintf('MOVE %d %d', startPos, endPos));
            if startsWith(response, "ERROR")
                obj.xAxisPosition   = startPos;
                obj.isZAxisExtended = false;
                obj.isGripperClosed = false;
                obj.isPlatePresent  = false;
            else
                obj.xAxisPosition   = 3;
                obj.isZAxisExtended = false;
                obj.isGripperClosed = true;
                obj.isPlatePresent  = false;
            end
        end

        function response = setTimeValues(obj, timeDelays)
            response = "";
            if ~isequal(size(timeDelays), [5 5])
                fprintf('Need a 5 by 5 matrix of time delays\n');
                return
            end
            % Same loop bounds as the original serial class
            for i = 1:5
                for j = 2:4
                    if i ~= j
                        response = obj.send(sprintf('SET_DELAY %d %d %d', ...
                            i, j, timeDelays(i,j)));
                        fprintf('%s\n', response);
                    end
                end
            end
        end

        function response = resetDefaultTimes(obj)
            response = obj.setTimeValues(obj.defaultTimeTable);
        end

        function response = getStatus(obj)
            response = obj.send('LOADER_STATUS');
        end

        function [xPos, zAxis, grip, plate] = getProperties(obj)
            xPos  = obj.xAxisPosition;
            zAxis = obj.isZAxisExtended;
            grip  = obj.isGripperClosed;
            plate = obj.isPlatePresent;
        end

        function response = shutdown(~)
            response = 'Disconnected';   % HTTP is stateless
        end
    end

    methods (Access = private)
        function response = send(obj, command)
            url = obj.BaseURL + "/api/" + strrep(string(command), " ", "%20");
            try
                resp = webread(url, obj.Options);
                if isstruct(resp)
                    resp = jsonencode(resp);
                end
                response = strtrim(string(resp));
            catch err
                response = "ERROR: " + string(err.message);
            end
        end
    end
end
