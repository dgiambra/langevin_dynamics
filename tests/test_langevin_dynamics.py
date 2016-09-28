#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_langevin_dynamics
----------------------------------

Tests for `langevin_dynamics` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from langevin_dynamics import langevin_dynamics
from langevin_dynamics import cli



class TestLangevin_dynamics(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'langevin_dynamics.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_func(self):
        self.assertFalse(langevin_dynamics.langevin_dynamics(1 , 1 , .01 , 1 , "example.txt" , 1 , 100)==10)
    def test_iterations(self):
        pos,vel,time = langevin_dynamics.langevin_dynamics(1,2,.01,1,"example.txt",1,100)
        self.assertTrue(len(pos)==100/.01)
    def test_type(self):
        pos,vel,time = langevin_dynamics.langevin_dynamics(1,2,.01,1,"example.txt",1,100)
        self.assertIsInstance(pos,list)

    #def test_invalidfile(self):
    #    self.assertRaises(IOError, langevin_dynamics.langevin_dynamics(1,1,.01,1,"doesnotcompute.txt",1,100))


if __name__ == '__main__':
    sys.exit(unittest.main())
