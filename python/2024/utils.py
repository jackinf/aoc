import os


def pr(output, *args, **kwargs):
    debug = os.environ.get('DEBUG', '0')
    if debug == '1':
        print(output, *args, **kwargs)