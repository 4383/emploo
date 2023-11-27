# -*- encoding: utf-8 -*-
import unittest

from emploo.__main__ import init


class TestInit(unittest.TestCase):
    def test_config(self):
        self.assertIn("Annotation", init())
