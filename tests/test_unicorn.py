from unittest import TestCase
from unicorn import matrix_to_bytes, bytes_to_matrix
from random import randint, randbytes


class UnicornTestCase(TestCase):

    def test_matrix_to_bytes(self):
        """
        Test the matrix_to_bytes function.
        """

        # Test on some defined inputs and outputs
        output1 = matrix_to_bytes([[(0, 0, 0)]])
        assert type(output1) == bytes
        assert output1 == b'\x00\x00\x00'
        output2 = matrix_to_bytes([[(0, 0, 0), (10, 20, 30)],
                                   [(255, 0, 255), (0, 255, 0)]])
        assert type(output2) == bytes
        assert output2 == b'\x00\x00\x00\n\x14\x1e\xff\x00\xff\x00\xff\x00'

        # Randomized test.
        input3 = []
        sub_list = []
        for i in range(8):
            for j in range(8):
                info1 = randint(0, 255)
                info2 = randint(0, 255)
                info3 = randint(0, 255)
                sub_list.append((info1, info2, info3))
            input3.append(sub_list)
            sub_list = []
        output3 = matrix_to_bytes(input3)
        assert type(output3) == bytes
        assert len(output3) == 192

    def test_bytes_to_matrix(self):
        """
        Test the bytes_to_matrix function.
        """

        # Test on some defined inputs and outputs
        output1 = bytes_to_matrix(b'\x00\x00\x00', 1, 1)
        assert type(output1) == list
        assert output1 == [[(0, 0, 0)]]
        output2 = bytes_to_matrix(
            b'\x00\x00\x00\n\x14\x1e\xff\x00\xff\x00\xff\x00', 2, 2
        )
        assert type(output2) == list
        assert output2 == [
            [(0, 0, 0), (10, 20, 30)],
            [(255, 0, 255), (0, 255, 0)]
        ]

        # Randomized test.
        input3 = randbytes(192)
        output3 = bytes_to_matrix(input3, 8, 8)
        assert len(output3) == 8
        assert len(output3[0]) == 8
        assert type(output3) == list
