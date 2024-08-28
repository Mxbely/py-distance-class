class Distance:
    def __init__(self, distance):
        self.km = distance

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            result = self.km + other.km
        else:
            result = self.km + other.real
        return Distance(
            distance=result
        )

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other.real
        return Distance(
            distance=self.km
        )

    def __mul__(self, other):
        if isinstance(other, Distance):
            return None
        else:
            return Distance(distance=self.km * other.real)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return None
        else:
            return Distance(distance=round(self.km / other.real, 2))

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other.real

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other.real

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other.real

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other.real

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other.real


# distance1 = Distance(30)
# distance2 = Distance(3)
# distance3 = distance1 / distance2
# print(distance2)
# print(repr(distance2))
# print(distance2)
