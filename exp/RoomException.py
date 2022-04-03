#!/usr/bin/env python3

class RoomException(Exception):
    """Exception for room reply"""
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

    def __repr__(self):
        return 'roomErr({})'.format(123)