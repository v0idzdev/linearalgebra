# Import math
import math


class Vector2D:

    """The Vector2D object we construct in the 
       __init__ method has cartesian co-ordinates"""

    # Vector2D constructor
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):  # Human readable string repr
        return '{:g}i + {:g}j'.format(self.x, self.y)

    def __repr__(self):  # Unambiguous string repr
        return repr((self.x, self.y))

    def dot(self, other):  # The dot product of two vectors

        if not isinstance(other, Vector2D):  # Raises error if not instance
            raise TypeError('Can only take dot product of two vectors')

        # Returns x and y vals multiplied respectively
        return self.x * other.x + self.y * other.y

    """Alias the __matmul__ method to dot so 
       we can use a @ b as well as a.dot(b)."""

    __matmul__ = dot

    def __sub__(self, other):  # Subtraction of two vectors
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):  # Addition of two vectors
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):  # Multiplies vector by scalar

        # If 'scalar' passed in is a scalar calculate product
        if isinstance(scalar, int) or isinstance(scalar, float):

            # Returns both components multiplies by scalar
            return Vector2D(self.x * scalar, self.y * scalar)

        # If 'scalar' passed in isn't actually a scalar throw an error
        raise NotImplementedError('Can only multiply Vector2D by a scalar')

    # Reflected multiplication
    def __rmul__(self, scalar):

        # Returns scalar * vector
        return self.__mul__(scalar)

    def __neg__(self):  # Invert through origin
        return Vector2D(-self.x, -self.y)

    def __truediv__(self, scalar):  # True division
        return Vector2D(self.x / scalar, self.y / scalar)

    def __mod__(self, scalar):  # Modulus by component
        return Vector2D(self.x % scalar, self.y % scalar)

    def __abs__(self):  # Magnitude of vector
        return math.sqrt(self.x**2 + self.y**2)

    # Distance between vectors
    def distance_to(self, other):

        # Subtract magnitudes
        return abs(self - other)

    def to_polar(self):  # Convert co-ordinates to polar
        return self.__abs__(), math.atan2(self.y, self.x)
