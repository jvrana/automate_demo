# PyDemo Automator

Runs scripted coded demos for your projects. Save your code as a file run `python run_demo.py`.
The script automates types to give the illusion of a human typing.

![example](images/pydemo.gif?raw=true)

## Usage

```bash
python run_demo.py <path_to_code> -r <float> -i <boolean>
```

- r: speed of run
- i: whether to ignore other comments
- a: whether to record video using asciinema

use `# wait 1` in code to wait for 1 seconds.

You can use something like giphy capture to grab your video.


Install [asciinema](https://asciinema.org/) with:
```bash
brew install asciinema
```

begin recording with:
```bash
asciinema rec
```
