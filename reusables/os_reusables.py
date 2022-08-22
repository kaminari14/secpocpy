import os, sys

def makedirectory(directory):
    try:
        os.mkdir(directory)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.stderr.write('error while creating diectory. Is directory already created? Continuing with the existing directory.')

