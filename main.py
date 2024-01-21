import board
import digitalio
import time
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

#Initializes all used HID inputs
mouse = Mouse(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

#Initializes and sets GPIO ports for buttons
button1= digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP6)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.GP12)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.GP28)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

button5 = digitalio.DigitalInOut(board.GP22)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

button6 = digitalio.DigitalInOut(board.GP18)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP

#Modify code for when button is pressed to whatever you like

while True:
    if not button1.value:
       #Code for Button 1
        kbd.press(Keycode.L)
        kbd.release_all()
    if not button2.value:
       #Code for Button 2
        kbd.press(Keycode.L)
        kbd.release_all()
    if not button3.value:
        #Code for Button3
        kbd.press(Keycode.L)
        kbd.release_all()
    if not button4.value:
        #Code for Button4
        kbd.press(Keycode.L)
        kbd.release_all()
    if not button5.value:
        #Code for Button5
        kbd.press(Keycode.L)
        kbd.release_all()
    if not button6.value:
        #Code for Button5
        kbd.press(Keycode.L)
        kbd.release_all()
    
       