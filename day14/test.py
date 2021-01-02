from unittest import TestCase

from day14.solution import apply_mask, decode_mem_address


class Day14TestSuite(TestCase):

    def test_apply_mask(self):
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        self.assertEqual(73, apply_mask(mask, 11))

    def test_decode(self):
        mask = '000000000000000000000000000000X1001X'
        self.assertEqual([26, 27, 58, 59], decode_mem_address(mask, 42))
