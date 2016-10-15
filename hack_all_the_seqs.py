import requests


def hack_what(thing_to_hack=None):
    if not thing_to_hack:
        thing_to_hack = "Hack all the Seqs!"
    return thing_to_hack

if __name__ == '__main__':
    hack_what()
