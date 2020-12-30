from unittest import TestCase

from day02.solution import _extract_params, _validate_password, _validate_password2


class Day02TestSuite(TestCase):

    def test_extract(self):
        line = '1-3 b: cdefg'

        params = _extract_params(line)

        self.assertEqual((1, 3, 'b', 'cdefg'), params)

    def test_validate(self):
        self.assertTrue(_validate_password(1, 3, 'b', 'abc'))
        self.assertFalse(_validate_password(1, 3, 'c', 'nope'))

    def test_validate2(self):
        self.assertTrue(_validate_password2(1, 3, 'a', 'abcde'))
        self.assertFalse(_validate_password2(1, 3, 'b', 'cdefg'))
        self.assertFalse(_validate_password2(2, 9, 'c', 'ccccccccc'))
