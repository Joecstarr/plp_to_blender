"""@@@TODO: ."""

from dataclasses import dataclass
from os import path


@dataclass
class PLPoint:
    """@@@TODO: ."""

    x: float
    y: float
    z: float

    def __eq__(self, other):
        """@@@TODO: ."""
        return (
            isinstance(other, PLPoint)
            and self.x == other.x
            and self.y == other.y
            and self.z == other.z
        )


class PLPath:
    """@@@TODO: ."""

    segements: list[list[PLPoint]]

    def __init__(self, path_str: str | None = None) -> None:
        """@@@TODO: ."""
        self.segements = [[]]
        if path_str:
            self.parse(path_str)

    def parse(self, path_str: str) -> None:
        """@@@TODO: ."""
        print(path_str.splitlines())
        for line in path_str.splitlines():
            if line == '':
                self.segements.append([])
            else:
                s = line.strip().split(',')
                self.segements[-1].append(
                    PLPoint(float(s[0]), float(s[1]), float(s[2]))
                )
