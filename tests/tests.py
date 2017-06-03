# -*- coding: utf-8 -*-
import unittest
import libkeepass
import keepass_guesser

# file : attempts from file expected before success or failure
guess_files = {'tests/data/guesslist0': {'attempts': 3, 'guessphrase': None},
               'tests/data/guesslist1': {'attempts': 1, 'guessphrase': 'test'},
               'tests/data/guesslist2': {'attempts': 2, 'guessphrase': 'test'},
               'tests/data/guesslist3': {'attempts': 3, 'guessphrase': 'test'}}
# kdb file : keyfile
kdbs = {'tests/data/test.kdbx': None,
        'tests/data/test_keyfile.kdbx': 'tests/data/test_keyfile'}


class TestSample(unittest.TestCase):
    def _test_kdb_file(self, kdb_file, key_file):
        with libkeepass.open(kdb_file, password="test",
                             keyfile=key_file) as kdb:
            self.assertEqual(kdb.opened, True)
            self.assertEqual(kdb.read(32), b'<?xml version="1.0" encoding="ut')

    def test_kdb_samples(self):
        """Test the test files"""
        for kdb_file, key_file in kdbs.iteritems():
            self._test_kdb_file(kdb_file, key_file)


class TestGuesser(unittest.TestCase):
    def test_kdb_samples(self):
        """Test the test files with try_guess"""
        for kdb_file, key_file in kdbs.iteritems():
            keepass_guesser.try_guess(kdb_file, 'test', key_file)

    def test_run(self):
        """Test the main run loop against each of the guess_files"""
        for kdb_file, key_file in kdbs.iteritems():
            for guess_file, expected in guess_files.iteritems():
                with open(guess_file, 'r') as guess_fh:
                    result, attempts = keepass_guesser.run(kdb_file, key_file,
                                                           guess_fh, False)
                    self.assertEqual(attempts, expected['attempts'])
                    self.assertEqual(result, expected['guessphrase'])

if __name__ == '__main__':
    unittest.main()
