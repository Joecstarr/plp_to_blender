"""Write functionality for database package."""

from peewee import SqliteDatabase

from .models.test import Test


def writeDB(db: str, wptt: str, path: str, blob: bytes):
    """Write the WPTT and PL path data to the database.

    Args:
        db: The database to write to.
        wptt: The WPTT for the PL path.
        path: The PL path string to write.
        blob: A blob containing the blender file data.
    """
    database = SqliteDatabase(db)
    database.bind([Test])

    with database:
        database.create_tables([Test])
        assert Test._meta.database is database
        if not Test.select().where(Test.wptt == wptt).exists():
            Test.create(wptt=wptt, PLPath=path, blenderBlob=blob)
