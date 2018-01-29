#!/usr/bin/env python3
"""
This file is part of 1Base.

1Base is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

1Base is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with 1Base.  If not, see <http://www.gnu.org/licenses/>.
"""

from mongoengine import (
    StringField
)
import re

RE_INT = re.compile(r'^\d+$').match


class IPAddressField(StringField):

    def validate(self, value, clean=True):
        """ Validate the IP address.

        Regexes are messy for IP addresses. We'll brute force validation.
        """
        parts = value.split('.')
        if len(parts) != 4:
            return False
        for p in parts:
            if len(p) > 3:
                return False
            if not RE_INT(p):
                return False
        return True
