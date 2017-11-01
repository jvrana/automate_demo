# PyDemo Automator

Runs scripted coded demos for your projects. Save your code as a file run `python run_demo.py`.
The script automates types to give the illusion of a human typing.

![example](images/pydemo.gif?raw=true)

## Usage

### Requirements

* [asciinema](https://asciinema.org/) (optional for autorecording of terminal)
    * `brew install asciinema`
* mac

### Installation

```bash
cd to/py_demo/dir
pip install .
```

### Usage

#### Run

```bash
pydemo filepath/to/your/code.py -r <speed> -i <ignore comments> -a <auto-record>
```

filepath: file path to your demo code

-r: speed of run

-i: whether to ignore other comments

-a: whether to record video using asciinema

#### Help

Run the following to get help with parameters:

```bash
python -h
```
