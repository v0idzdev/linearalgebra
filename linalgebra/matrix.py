# IMPORTS BASIC MODULES WE NEED
from random import randrange
import operator
import sys


class Matrix:

    # Constructor for a matrix
    def __init__(self, m, n, init=True):

        if init:  # 'm' is amount of rows, 'n' is cols
            self.rows = [[0] * n for x in range(m)]

        else:  # Else make empty
            self.rows = []

        self.m = m
        self.n = n

    # Get and set item methods

    def __getitem__(self, index):  # Gets index
        return self.rows[index]  # Returns at index

    def __setitem__(self, index, val):  # Gets index
        self.rows[index] = val  # Sets item at the index

    # String parsing and representation

    def __str__(self):  # Parses the matrix into a string
        string_ = '\n'.join([' '.join([str(item) for item in row])
                             for row in self.rows])

        # Returns the string
        return string_ + '\n'

    def __repr__(self):  # Creates printable string repr of matrix
        string_ = str(self.rows)  # Parses each row into a string
        rank = str(self.get_rank())  # Gets the rank of the string
        rep = "Matrix: \"%s\", rank: \"%s\"" % (string_, rank)

        # Returns
        return rep

    def reset(self):  # Resets the matrix data
        self.rows = [[] for x in range(self.m)]

    # Transpose and get transpose methods

    """Transpose transposes the original matrix,
       and changes it. Get transpose returns the 
       transposition of the matrix, but without
       modifying the original matrix in any way."""

    def transpose(self):  # Transposes the matrix, but changes it
        self.m, self.n = self.n, self.m  # Flips matrix over diagonal
        self.rows = [list(item) for item in zip(*self.rows)]

    def get_transpose(self):
        m, n = self.n, self.m
        matrix = Matrix(m, n)  # Creates new object for return
        matrix.rows = [list(item) for item in zip(*self.rows)]

        # Returns
        return matrix

    def get_rank(self):  # Gets rank
        return (self.m, self.n)

    # Matrix operator overload methods

    def __eq__(self, matrix):  # Equality test
        return (self.rows == matrix.rows)

    """Adds another matrix to the current matrix
       without returning a new one. The following
       method simply returns the operation's result."""

    def __add__(self, matrix):  # Addition operator

        # If ranks aren't equal, raise exception
        if self.get_rank() != matrix.get_rank():
            raise TypeError("Ranks must be equal.")

        # Sets up a matrix for return
        return_ = Matrix(self.m, self.n)

        # Adds the matrices
        for x in range(self.m):

            # Add each element from both matrices
            for item in zip(self.rows[x], matrix[x]):
                row = [item[0] + item[1]]

            # Return[x] equals row
            return_[x] = row

        # Returns result
        return return_

    """Subtracts another matrix from current matrix
       without returning a new one. The following
       method simply returns the operation's result."""

    def __sub__(self, matrix):  # Addition operator

        # If ranks aren't equal, raise exception
        if self.get_rank() != matrix.get_rank():
            raise TypeError("Ranks must be equal.")

        # Sets up a matrix for return
        return_ = Matrix(self.m, self.n)

        # Adds the matrices
        for x in range(self.m):

            # Subtract each element from the matrix
            for item in zip(self.rows[x], matrix[x]):
                row = [item[0] - item[1]]

            # Return[x] equals row
            return_[x] = row

        # Returns result
        return return_

    """Multiplies a matrix with the current matrix
       without returning a new one. The following
       method simply returns the operation's result."""

    def __mul__(self, matrix):  # Multiply operator

        mat_m, mat_n = matrix.get_rank()

        if self.n != mat_m:  # If can't be multiplied
            raise TypeError("Can't be multiplied.")

        mat_t = matrix.get_transpose()
        mul_matrix = Matrix(self.m, mat_n)

        # Multiplies the matrix
        for x in range(self.m):
            for y in range(mat_t.m):
                mul_matrix[x][y] = sum([item[0]*item[1]
                                       for item in zip(self.rows[x], mat_t[y])])

        # Returns the result
        return mul_matrix

    """The following overloads modify the current
       matrix after the operation has been carried
       out. And then return that value."""

    # Addition w/ modification
    def __iadd__(self, matrix):
        temp = self + matrix
        self.rows = temp.rows[:]
        return self

    # Subtraction w/ modification
    def __isub__(self, matrix):
        temp = self - matrix
        self.rows = temp.rows[:]
        return self

    # Multiply w/ modification
    def __imul__(self, matrix):
        temp = self * matrix
        self.rows = temp.rows[:]
        self.m, self.n = temp.get_rank()
        return self

    """The following methods are class mathods
       and are static, so they do not have to 
       be bound to an object like the methods
       that are listed above."""

    @classmethod  # Makes matrix
    def _make_matrix(cls, rows):
        n = len(rows[0])
        m = len(rows)

        # If row length inconsistent raise error
        if any([len(row) != n for row in rows[1:]]):
            raise TypeError("Inconsistent row length")

        # Makes an empty matrix
        matrix = Matrix(m, n, init=False)
        matrix.rows = rows

    @classmethod  # Makes random matrix
    def make_random(cls, m, n, low=0, high=10):
        obj = Matrix(m, n, init=False)

        for x in range(m):
            for i in range(obj.n):
                obj.rows.append([randrange(low, high)])

        # Returns
        return obj

    @classmethod  # Make zero matrix
    def make_zero(cls, m, n):

        # Make zero matrix of rank mxm
        rows = [[0] * m for x in range(m)]
        return cls.from_list(rows)

    @classmethod  # Makes identity matrix
    def make_id(cls, m, n):

        rows = [[0] * m for x in range(m)]
        index = 0

        for row in rows:
            row[index] = 1
            index += 1

        return cls.from_list(rows)

    @classmethod
    def read_std_in(cls):

        # Reads a matrix's values from standard input
        print("Enter a matrix row by row, type Q to quit")
        rows = []  # Initialise empty list

        while True:  # Reads input
            line = sys.stdin.readline().strip()
            if line == "Q" or line == "q":
                break  # Stops on quit

            # Puts the input into the list
            row = [int(x) for x in line.split()]
            rows.append(row)

        # Calls the make matrix method
        return cls._make_matrix(rows)

    @classmethod  # Reads from file
    def read_grid(cls, fname):

        rows = []  # Adds to empty list
        for line in open(fname).readlines():
            row = [int(x) for x in line.split()]
            rows.append(row)

        # Calls the make matrix method
        return cls._make_matrix(rows)

    @classmethod  # Makes matrix from list of lists
    def from_list(cls, list_of_lists):

        # Constructs matrix
        rows = list_of_lists[:]
        return cls._make_matrix(rows)
