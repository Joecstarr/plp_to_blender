"""PL Path package."""

from .plpoint import PLPoint


class PLPath:
    """PL path container class.

    Contains a list of segments which are themselves lists of points.

    Attributes:
        segments: The list of segments.
    """

    segments: list[list[PLPoint]]

    def __init__(self, path_str: str | None = None) -> None:
        """Initialize the module.

        Args:
            path_str: An optional PL path encoded as a string.
        """
        self.segments = [[]]
        if path_str:
            self.parse(path_str)

    def parse(self, path_str: str) -> None:
        """Parse a PL string into segments of points.

        Args:
            path_str: The input PL path string.
        """
        # for each line in the PL path string
        for line in path_str.splitlines():
            # if the line is empty we need a new segment
            if line == '':
                self.segments.append([])
            else:
                split_line = line.strip().split(',')
                self.segments[-1].append(
                    PLPoint(
                        float(split_line[0]), float(split_line[1]), float(split_line[2])
                    )
                )
