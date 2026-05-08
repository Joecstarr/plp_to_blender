"""Main calling routines with typer interfaces."""

from pathlib import Path

import typer

from .blender_handler.build import blend
from .blender_handler.out_blob import blendBlob
from .blender_handler.out_file import saveBlendFile
from .db_handler.db import writeDB
from .path_parsing.plpath import PLPath


def convert(pathStr: str = '', dbFile: str = '', wptt: str = '', outputFile: str = ''):
    """Load into blender an input PL path.

    Args:
        pathStr: The PL as a raw string.
        dbFile: A path to an SQLite database for storage.
        wptt: The WPTT for the input PL path.
        outputFile: A path to a blender file to output to.

    Raises:
        ValueError: A PL path is not loaded.
    """
    if not pathStr:
        while True:
            try:
                pathStr = pathStr + input() + '\n'
            except EOFError:
                break

    if not pathStr:
        raise ValueError('There is no PL path to process.')

    path = PLPath(pathStr)
    blend(path)

    if outputFile:
        saveBlendFile(Path(outputFile))

    if wptt and dbFile:
        blob = blendBlob()
        writeDB(dbFile, wptt, pathStr, blob)


if __name__ == '__main__':
    typer.run(convert)
