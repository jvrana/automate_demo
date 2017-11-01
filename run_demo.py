from appscript import app, k
import random
import time
import re
import hug
import os

RETURN = '\r'

@hug.cli()
def run_demo(filepath: hug.types.text, speed: hug.types.float_number=1.0, ignore_comments:
hug.types.smart_boolean=False, python: hug.types.smart_boolean=True, asciicast: hug.types.smart_boolean=True):

    filepath = os.path.abspath(filepath)
    if not os.path.isfile(filepath):
        raise FileNotFoundError("Cannot run demo. File not found: {}".format(filepath))

    terminal = app("Terminal")
    terminal.activate()
    time.sleep(1.0)
    sysevents = app("System Events")

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
                print("  ignoring commenct")
                return
        for char in line:
            sysevents.keystroke(char)
            time.sleep(random.uniform(*_mult(keystroke_delay)))
        time.sleep(random.uniform(*_mult(return_delay)))
        if with_return:
            sysevents.keystroke(RETURN)

    if asciicast:
        print("recording using asciicast...")
        type_line('asciinema rec', with_return=True)
        time.sleep(1)

    print("running demo {}".format(os.path.abspath(filepath)))
    if python:
        type_line("python", with_return=True)
        time.sleep(*_mult(python_start_delay))

    lines = []
    with open(filepath, 'rU') as f:
        lines = f.readlines()


    for line in lines:
        type_line(line)

    if asciicast:
        sysevents.keystroke('d', using=[k.control_down])
        type_line('exit', with_return=True)
        time.sleep(1)
        sysevents.keystroke(RETURN)

def main():
    run_demo.interface.cli()

if __name__ == '__main__':
    main()