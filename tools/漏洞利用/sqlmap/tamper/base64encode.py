#!/usr/bin/env python

"""
Copyright (c) 2006-2022 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.convert import encodeBase64
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Base64-encodes all characters in a given payload

    >>> tamper("1' AND SLEEP(5)#")
    'MScgQU5EIFNMRUVQKDUpIw=='
    """

    return encodeBase64(payload, binary=False) if payload else payload
