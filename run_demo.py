from appscript import app, k
import random
import time
import re
import hug
import os
from AppKit import NSWorkspace


RETURN = '\r'
TERMINAL = app("Terminal")
SYSEVENTS = app("System Events")

def open_terminal(cd):
    TERMINAL.run()
    time.sleep(0.5)
    TERMINAL.activate()
    time.sleep(0.5)
    SYSEVENTS.keystroke('n', using=k.command_down)
    time.sleep(0.1)
    SYSEVENTS.keystroke('cd {}'.format(cd) + RETURN)
    time.sleep(0.05)

def curr_window():
    return NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()

@hug.cli()
def run_demo(filepath: hug.types.text, speed: hug.types.float_number=1.0, ignore_comments:
hug.types.smart_boolean=False, python: hug.types.smart_boolean=False, asciicast: hug.types.smart_boolean=True,
             cd: hug.types.text=''):

    filepath = os.path.abspath(filepath)
    if not os.path.isfile(filepath):
        raise FileNotFoundError("Cannot run demo. File not found: {}".format(filepath))

    filedir = os.path.dirname(filepath)
    if cd == '':
        cd = filedir
    open_terminal(cd)

    python_start_delay = (0.5,)
    keystroke_delay = (0.02, 0.1)
    return_delay = (0.4, 0.6)

    def _mult(t):
        return [float(x) / speed for x in list(t)]

    def type_line(line, with_return=False):
        print("printing line \"{}\"".format(line.strip()))
        if line.strip().startswith('#'):
            m = re.match("# wait\s+(\d+\.?\d*)", line)
            if m:
                time.sleep(float(m.group(1)) / float(speed))
                print("  waiting for {}s".format(m.group(1)))
                return
            if ignore_comments:
                print("  ignoring comment")
                return
        for char in line:
            SYSEVENTS.keystroke(char)
            time.sleep(random.uniform(*_mult(keystroke_delay)))
        time.sleep(random.uniform(*_mult(return_delay)))
        if with_return:
            SYSEVENTS.keystroke(RETURN)

    if asciicast:
        print("recording using asciicast...")
        type_line('asciinema rec', with_return=True)
        time.sleep(1)

    print("running demo {}".format(os.path.abspath(filepath)))
    if python:
        SYSEVENTS.keystroke('python'+RETURN)
        time.sleep(*_mult(python_start_delay))

    lines = []
    with open(filepath, 'rU') as f:
        lines = f.readlines()


    for line in lines:
        if not curr_window() == TERMINAL.name.get():
            print("demo cancelled.")
            return
        type_line(line)

    if asciicast:
        SYSEVENTS.keystroke('d', using=[k.control_down])
        time.sleep(0.1)
        SYSEVENTS.keystroke('exit'+RETURN)
        time.sleep(1)
        SYSEVENTS.keystroke(RETURN)

def main():
    run_demo.interface.cli()

if __name__ == '__main__':
    main()