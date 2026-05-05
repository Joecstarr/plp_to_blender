"""@@@TODO: ."""

from pathlib import Path

import typer

from plp2blender.mkblender import blend, blendBlob, saveBlendFile

from .plpath_parsing import PLPath


def convert(path_str: str = '', path_file: str = ''):
    """@@@TODO: ."""

    if path_file:
        with open(path_file, 'r') as fr:
            path_str = fr.read()

    if not path_str:
        while True:
            try:
                path_str = path_str + input() + '\n'
            except EOFError:
                # no more information
                break

    if not path_str:
        raise ValueError('A very specific bad thing happened.')

    path = PLPath(path_str)
    blend(path)
    blob = blendBlob()
    saveBlendFile(Path('out.blend'))
    ...


if __name__ == '__main__':
    typer.run(convert)
