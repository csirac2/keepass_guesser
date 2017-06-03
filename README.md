keepass_guesser
===============

A slow and stupid keepass brute-forcer using [libkeepass](https://github.com/libkeepass/libkeepass)

[![Build Status](https://travis-ci.org/csirac2/keepass_guesser.svg?branch=master)](https://travis-ci.org/csirac2/keepass_guesser)

Seriously, go use hashcat instead. This is just a few lines around the hard work of libkeepass.

### Examples

These are using the test data .kdbx which have the passphrase `test`.

Run the tests. This should set up a virtualenv you could activate with `. env/bin/activate` if you wanted to run keepass_guesser that way. You'll likely need some build dependencies for libkeepass using lxml such as python2-dev, libxml2-dev, libxslt1-dev, etc.

    make test

Simplest example:

    $ ./keepass_guesser.py tests/data/test.kdbx tests/data/guesslist3
    SUCCESS after 3 attempts:
    test

With a keyfile:

    $ ./keepass_guesser.py --keyfile=tests/data/test_keyfile tests/data/test_keyfile.kdbx tests/data/guesslist2
    SUCCESS after 2 attempts:
    test

When the guesslist file does not contain the passphrase:

    $ ./keepass_guesser.py --keyfile=tests/data/test_keyfile tests/data/test_keyfile.kdbx tests/data/guesslist0
    Unsuccessful after 3 attempts

RTFM

    $ ./keepass_guesser.py -h
    usage: keepass_guesser.py [-h] [--keyfile KEYFILE] [-v] keepfile guessfile

    A slow and stupid keepass brute-forcer.

    positional arguments:
      keepfile           .kdb[x] file compatible with libkeepass
      guessfile          Newline separated file of each passphrase to try

    optional arguments:
      -h, --help         show this help message and exit
      --keyfile KEYFILE  keyfile for the keepfile
      -v, --verbose      debug output

This project uses the 2-clause Simplified BSD License.
