import unittest
import eulersolver


class EulerSolverTestCase(unittest.TestCase):
    def test_solves_problem_one(self):
        solver = eulersolver.EulerSolver()

        result = solver.solve_problem_one()

        self.assertEqual(result, 233168)

    def test_find_sum_of_multiples_of_4_and_limit_10_should_be_12(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_sum_of_multiples(10, [4])

        self.assertEqual(result, 12)

    def test_find_sum_of_multiples_of_3_5_and_limit_10_should_be_23(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_sum_of_multiples(10, [3, 5])

        self.assertEqual(result, 23)

