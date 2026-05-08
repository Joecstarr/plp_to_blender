"""PL Point package."""

from dataclasses import dataclass


@dataclass
class PLPoint:
    """PL path point container class.

    Attributes:
        x: The $x$ coordinate.
        y: The $y$ coordinate.
        z: The $z$ coordinate.
    """

    x: float
    y: float
    z: float

    def __eq__(self, other):
        """Equality operator for the point class.

        Args:
            other: The object to compare to.

        Returns:
            Truth value of the comparison.

        """
        return (
            isinstance(other, PLPoint)
            and self.x == other.x
            and self.y == other.y
            and self.z == other.z
        )
