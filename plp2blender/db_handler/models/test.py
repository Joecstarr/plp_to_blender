"""Test case data."""

from peewee import (
    BlobField,
    Model,
    TextField,
)

database = None


class Test(Model):
    """ORM for a single test dataset.

    Attributes:
        wptt: A WPTT for the test.
        blenderBlob: A blob containing blender file data.
        PLPath:  A PL path string.
    """

    wptt = TextField()
    blenderBlob = BlobField()
    PLPath = TextField()
