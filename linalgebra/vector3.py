import math


class Vector3D:

    """The Vector3D object we construct in the 
       __init__ method has cartesian co-ordinates"""

    # Vector3D constructor
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):  # Converts to a human readable string
        return '{:g}i + {:g}j + {:g}k'.format(self.x, self.y, self.z)

    def __repr__(self):  # Unambiguous string representation
        return repr((self.x, self.y, self.z))  # Returns as tuple

    def dot(self, other):  # The dot product of two 3D vectors

        if not isinstance(other, Vector3D):  # Raises error if not instance
            raise TypeError('Can only take dot product of two vectors')

        # Then returns the x, y and z values multiplied respectively
        return self.x * other.x + self.y * other.y + self.z * other.z

    """Alias the __matmul__ method to dot so 
       we can use a @ b as well as a.dot(b)."""

    __matmul__ = dot

    def __sub__(self, other):  # Subtraction of two 3 dimensional vectors
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):  # Addition of two 3 dimensional vectors
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar):  # Multiplies 3D vector by scalar

        # If 'scalar' passed in is a scalar calculate product
        if isinstance(scalar, int) or isinstance(scalar, float):

            # Returns all three vector components multiplied by the scalar
            return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

        # If 'scalar' passed in isn't actually a scalar throw an error
        raise NotImplementedError('Can only multiply Vector3D by a scalar')

    # Reflected multiplication
    def __rmul__(self, scalar):

        # Returns scalar * vector
        return self.__mul__(scalar)

    def __neg__(self):  # Invert 3D vector through origin
        return Vector3D(-self.x, -self.y, -self.z)

    def __truediv__(self, scalar):  # True division of two 3D vectors
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def __mod__(self, scalar):  # Modulus of a 3D vector by a scalar
        return Vector3D(self.x % scalar, self.y % scalar, self.z % scalar)

    def __abs__(self):  # The magnitude of a 3D vector
        return math.sqrt(self.x**2 + self.y**2, self.z**2)

    # Distance between two vectors
    def distance_to(self, other):

        # Subtract magnitudes
        return abs(self - other)

    def to_polar(self):  # Convert 3D vector co-ordinates to polar
        return self.__abs__(), math.atan(self.y / self.x / self.z)
