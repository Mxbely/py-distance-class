from __future__ import annotations


class Distance:
    def __init__(self, distance: int | float) -> None:
        self.km = distance

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other.real
        return Distance(distance=self.km)

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other.real
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(distance=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(distance=round(self.km / other, 2))

    def __eq__(self, other: int | float) -> bool:
        return self.km == other

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        return self.km >= other
