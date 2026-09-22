import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 19200, timeout=10)  # python -m serial.tools.miniterm
time.sleep(1.0)  # Necessary sometimes :)
ser.reset_input_buffer()

def send_command(command):
    """Send a command string over serial and return the response."""
    message_bytes = (command + "\n").encode()
    ser.write(message_bytes)

    response_bytes = ser.readline()
    response = response_bytes.decode().strip()
    print(response)
    return response

def ResetOption():
    send_command("RESET")

def XAxisSubMenu():
    print("\nSelect X-Axis value:")
    print("Position 1")
    print("Position 2")
    print("Position 3")
    print("Position 4")
    print("Position 5")
    sub_choice = input("Enter your choice (1-5): ")

    if sub_choice in ("1", "2", "3", "4", "5"):
        return sub_choice
    else:
        print("Invalid choice. Please try again.")
        return None
    
def ZAxisSubMenu():
    print("\nSelect Z-Axis Position:")
    print("1. Extended")
    print("2. Retracted")
    sub_choice = input("Enter your choice: ")

    if sub_choice in ("1", "2"):
        return sub_choice
    else:
        print("Invalid choice. Please try again.")
        return None

def GripperSubMenu():
    print("\n Select Gripper Position:")
    print("1. Open")
    print("2. Close")
    sub_choice = input("Enter your choice: ")

    if sub_choice in ("1", "2"):
        return sub_choice
    else:
        print("Invalid choice. Please try again.")
        return None

def MoveSubMenu1():
    print("\n Select Move From Position:")
    print("Position 1")
    print("Position 2")
    print("Position 3")
    print("Position 4")
    print("Position 5")
    move_from_choice = input("Enter your choice: ")

    if move_from_choice in ("1", "2","3","4","5"):
        return move_from_choice
    else:
        print("Invalid choice. Please try again.")
        return None

def MoveSubMenu2():
    print("\n Select Move To Position:")
    print("Position 1")
    print("Position 2")
    print("Position 3")
    print("Position 4")
    print("Position 5")
    move_to_choice = input("Enter your choice: ")

    if move_to_choice in ("1", "2","3","4","5"):
        return move_to_choice
    else:
        print("Invalid choice. Please try again.")
        return None
    
def XAxisOption():
    value = None
    while value is None:
        value = XAxisSubMenu()

    # Sends something like "X-AXIS 3"
    send_command(f"X-AXIS {value}")

def ZAxisOption():
    value = None
    while value is None:
        value = ZAxisSubMenu()

    # Sends something like "Z-AXIS EXTEND"
    if value == "1":
        send_command(f"Z-AXIS EXTEND")
    elif value == "2":
        send_command(f"Z-AXIS RETRACT")

def GripperOption():
    value = None
    while value is None:
        value = GripperSubMenu()

    # Sends something like "GRIPPER OPEN"
    if value == "1":
        send_command(f"GRIPPER OPEN")
    elif value == "2":
        send_command(f"GRIPPER CLOSE")

def MoveOption():
    move_from_value = None
    move_to_value = None

    while move_from_value is None:
        move_from_value = MoveSubMenu1()
    while move_to_value is None:
        move_to_value = MoveSubMenu2()

    send_command(f"MOVE {move_from_value} {move_to_value}")

def display_menu():
    print("\n1. Reset")
    print("2. X-Axis")
    print("3. Z-Axis")
    print("4. Gripper")
    print("5. Move")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        ResetOption()
    elif choice == "2":
        XAxisOption()
    elif choice == "3":
        ZAxisOption()
    elif choice == "4":
        GripperOption()
    elif choice == "5":
        MoveOption()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

ser.close()