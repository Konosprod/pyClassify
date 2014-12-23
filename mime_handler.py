#!/usr/bin/python3.3

import magic
import sys

def getMime(filename):
    ret = ""
    mime = magic.open(magic.MAGIC_MIME)
    mime.load()
    ret = mime.file(filename).split(";")[0]
    return ret

