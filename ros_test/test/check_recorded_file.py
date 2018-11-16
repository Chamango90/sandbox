#!/usr/bin/env python
PKG = "ros_test"
NAME = "check_recorded_file"

# import rospy
import unittest, rostest

import sys


class CheckRecordedFile(unittest.TestCase):
    def test_one_equals_one(self):
        self.assertEquals(1, 1, "1!=1")


if __name__ == "__main__":
    rostest.rosrun(PKG, NAME, CheckRecordedFile, sys.argv)
