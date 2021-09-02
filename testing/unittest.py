from linalgebra import Matrix  # Import matrix
import unittest  # Import unit test module


class MatrixTests(unittest.TestCase):

    def testAdd(self):
        m1 = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix.from_list([[7, 8, 9], [10, 11, 12]])
        m3 = m1 + m2
        self.assert_true(m3 == Matrix.from_list([[8, 10, 12], [14, 16, 18]]))

    def testSub(self):
        m1 = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix.from_list([[7, 8, 9], [10, 11, 12]])
        m3 = m2 - m1
        self.assert_true(m3 == Matrix.from_list([[6, 6, 6], [6, 6, 6]]))

    def testMul(self):
        m1 = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix.from_list([[7, 8], [10, 11], [12, 13]])
        self.assert_true(m1 * m2 == Matrix.from_list([[63, 69], [150, 165]]))
        self.assert_true(
            m2*m1 == Matrix.from_list([[39, 54, 69], [54, 75, 96], [64, 89, 114]]))

    def testTranspose(self):

        m1 = Matrix.make_random(25, 30)
        zerom = Matrix.make_zero(25, 30)
        m2 = m1 + zerom

        m1.transpose()
        m1.transpose()
        self.assert_true(m2 == m1)

        # Also test get_transpose
        m2 = m1.get_transpose()
        r2 = m2.get_rank()

        self.assert_true(r2 == (30, 25))
        m2.transpose()

        self.assert_true(m2 == m1)

    def testId(self):

        m1 = Matrix.make_id(10)
        m2 = Matrix.make_random(4, 10)
        m3 = m2*m1
        self.assert_true(m3 == m2)


if __name__ == "__main__":
    unittest.main()
