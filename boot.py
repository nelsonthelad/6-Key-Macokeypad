import storage, usb_cdc
import board, digitalio

shutOff = digitalio.DigitalInOut(board.GP18)
shutOff.direction = digitalio.Direction.INPUT
shutOff.pull = digitalio.Pull.UP

if shutOff.value:
    storage.disable_usb_drive()
    usb_cdc.disable()