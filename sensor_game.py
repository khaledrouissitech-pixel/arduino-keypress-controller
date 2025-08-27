import serial
import keyboard

# Change COM to your Arduino port:

arduino = serial.Serial("COM5", 9600)

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()

        if data == "1":
            keyboard.press("r")
            print("Sensor triggered → R pressed")
        else:
            keyboard.release("r")
            print("Sensor off → R released")
