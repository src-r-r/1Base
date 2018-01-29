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

from onebase_presenter import fieldss

from mongoengine import (
    Document
)


class Client(Document):

    # For now ID will be an I.P address field. I'd like to make
    # IDs I.P.-independent in the future (for privacy & convenience),
    # But for now the're IP's.
    # - Jordan Hewitt <jordan.h@startmail.com>
    id = fields.IPAddressField()


class
