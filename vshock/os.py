import atexit
import os


def create_fifo(path):
    """
    Make an fifo(named pipe) at specific path.
    And remove it at exit.
    """
    os.mkfifo(path)
    atexit.register(os.unlink, path)

