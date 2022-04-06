from unittest import TestCase


class SnakeTestCase(TestCase):

    def test_matrix_to_bytes(self):
        from send_unicorn import matrix_to_bytes
        import random
        output1 = matrix_to_bytes([[(0, 0, 0)]])
        assert output1 == b'\x00\x00\x00'
        output2 = matrix_to_bytes([[(0, 0, 0), (10, 20, 30)],
                                   [(255, 0, 255), (0, 255, 0)]])
        assert output2 == b'\x00\x00\x00\n\x14\x1e\xff\x00\xff\x00\xff\x00'

        input3 = []
        sub_list = []
        for i in range(8):
            for j in range(8):
                info1 = random.randint(0, 255)
                info2 = random.randint(0, 255)
                info3 = random.randint(0, 255)
                sub_list.append((info1, info2, info3))
            input3.append(sub_list)
            sub_list = []

        output3 = matrix_to_bytes([[(0, 0, 0), (10, 20, 30)],
                                   [(255, 0, 255), (0, 255, 0)]])
        assert type(output1) == bytes
        assert type(output2) == bytes
        assert type(output3) == bytes
