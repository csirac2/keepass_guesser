#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
from argparse import ArgumentParser
import libkeepass
import sys


def __get_parser():
    # command line option parsing
    parser = ArgumentParser(description='A slow and stupid keepass guesser')
    parser.add_argument(
        'keepfile',
        help='.kdb[x] file compatible with libkeepass')
    parser.add_argument(
        'guessfile', type=file,
        help='Newline separated file of each passphrase to try')
    parser.add_argument(
        '--keyfile', required=False,
        help='keyfile for the keepfile')
    parser.add_argument('-v', '--verbose', help='debug output',
                        default=False, action="store_true")

    return parser


def try_guess(keepfile, guessphrase, keyfile=None):
    with libkeepass.open(keepfile, password=guessphrase, keyfile=keyfile):
        return True
    return False


def run(keepfile, keyfile, guessfile_fh, verbose):
    guessphrase = None
    attempts = 0
    for guessphrase in guessfile_fh:
        guessphrase = guessphrase.rstrip('\n')
        success = False
        try:
            if verbose is True:
                print ('Trying "{}"...'.format(guessphrase))
            attempts += 1
            success = try_guess(keepfile, guessphrase, keyfile)
            break
        except IOError as e:
            if e.message == 'Master key invalid.':
                if verbose is True:
                    print ('Failed: "{}"'.format(guessphrase))
            else:
                raise e

    if success is True:
        return guessphrase, attempts
    else:
        return None, attempts

if __name__ == '__main__':
    parser = __get_parser()
    args = vars(parser.parse_args())
    guessphrase, attempts = run(args['keepfile'], args['keyfile'],
                                args['guessfile'], args['verbose'])
    if guessphrase is not None:
        print('SUCCESS after {} attempts:'.format(attempts), file=sys.stderr)
        print(guessphrase)
        exit(0)
    else:
        print('Unsuccessful after {} attempts'.format(attempts),
              file=sys.stderr)
        exit(1)
