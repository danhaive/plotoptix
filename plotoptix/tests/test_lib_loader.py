import platform

from unittest import TestCase
from plotoptix._load_lib import load_optix

class TestScene(TestCase):

    def test000_load_optix(self):
        optix = load_optix()
        self.assertTrue(optix is not None, msg="RnD.SharpOptiX not loaded.")
        self.assertTrue(optix.test_library(123), msg="RnD.SharpOptiX test function failed.")
