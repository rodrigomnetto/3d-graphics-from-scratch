from dataclasses import dataclass
from typing import Sequence


@dataclass
class Polygon:
    """A polygon described by its vertices and drawing color."""

    vertices: Sequence[tuple[float, float, float]]
    color: tuple[int, int, int]
