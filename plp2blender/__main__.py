"""@@@TODO: ."""

import typer

from .plpath_parsing import PLPath


def convert(path_str: str = ''):
    """@@@TODO: ."""
    if not path_str:
        while True:
            try:
                path_str = path_str + input() + '\n'
            except EOFError:
                # no more information
                break
    path = PLPath(path_str)


if __name__ == '__main__':
    typer.run(convert)
