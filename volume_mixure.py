import keyboard
# print(keyboard.read_hotkey()); input()
#сам скрипт
keyboard.add_hotkey("ctrl+up", lambda:keyboard.send("volume up"))
keyboard.add_hotkey("", lambda:keyboard.send("volume down"))
keyboard.add_hotkey("", lambda:keyboard.send("volume mute"))
input()