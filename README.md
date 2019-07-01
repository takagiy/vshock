# How it works
First, vshock creates a unix fifo(named pipe) in the specific path. Then it sends pseudo input data to the fifo according to your instructions in the web UI.

# Requiement
* python3
* pip (or manually install docopt and tornado)

# Installation
```console
sudo pip install vshock
```

# Usage

```console
Usage:
  vshock <path> [options]

Where:
  <path> is the location to make input stream of the virtual controller.

Options:
  -h --help       Show this help.
  --port <number> Specify the port number to listen.
  -b --browser    Open the browser automatically.
```
