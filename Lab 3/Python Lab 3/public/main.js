async function sendCommand(command){
    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log(replyText);
    document.querySelector("#replyText").innerHTML = replyText;
    return replyText
}

function main() {
    console.log("Hello JavaScript");
    //document.querySelector("#ResetButton").innerHTML = "Different";
    document.querySelector("#Reset").onclick = () => {
        console.log("Reset button clicked");
        sendCommand("RESET");
    }
    document.querySelector("#XAxis1").onclick = () => {
        console.log("X Axis 1 button clicked");
        sendCommand("X-AXIS 1");
    }
    document.querySelector("#XAxis2").onclick = () => {
        console.log("X Axis 2 button clicked");
        sendCommand("X-AXIS 2");
    }
    document.querySelector("#XAxis3").onclick = () => {
        console.log("X Axis 3 button clicked");
        sendCommand("X-AXIS 3");
    }
    document.querySelector("#XAxis4").onclick = () => {
        console.log("X Axis 4 button clicked");
        sendCommand("X-AXIS 4");
    }
    document.querySelector("#XAxis5").onclick = () => {
        console.log("X Axis 5 button clicked");
        sendCommand("X-AXIS 5");
    }
    document.querySelector("#XAxis1").onclick = () => {
        console.log("X Axis 1 button clicked");
        sendCommand("X-AXIS 1");
    }
    document.querySelector("#ZAxisExtend").onclick = () => {
        console.log("Z Axis Extend button clicked");
        sendCommand("Z-AXIS EXTEND");
    }
    document.querySelector("#ZAxisRetract").onclick = () => {
        console.log("Z Axis Retract button clicked");
        sendCommand("Z-AXIS RETRACT");
    }
    document.querySelector("#GripperOpen").onclick = () => {
        console.log("Gripper Open button clicked");
        sendCommand("GRIPPER OPEN");
    }
    document.querySelector("#GripperClose").onclick = () => {
        console.log("Gripper Close button clicked");
        sendCommand("GRIPPER CLOSE");
    }
    document.querySelector("#Status").onclick = () => {
        console.log("Status button clicked");
        sendCommand("LOADER_STATUS");
    }
    document.querySelector("#Move").onclick = () => {
        var startPos = document.querySelector("#moveFrom").value;
        var endPos = document.querySelector("#moveTo").value;
        console.log(`Move button clicked from ${startPos} to ${endPos}`);
        sendCommand(`MOVE ${startPos} ${endPos}`);
    }

}

main();