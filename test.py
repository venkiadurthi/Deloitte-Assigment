import unittest
from main import raindrops
class RaindropsTest (unittest.TestCase):

    #Testing numbers with Factors of 3
    def test_for_3(self):
        self.assertEqual(raindrops(3), "Pling")
    def test_for_(self):
        self.assertEqual(raindrops(6), "Pling")
    def test_for_9(self):
        self.assertEqual(raindrops(9), "Pling")
    def test_for_27(self):
        self.assertEqual(raindrops(27), "Pling")

    #Testing numbers with Factors of 5
    def test_for_5(self):
        self.assertEqual(raindrops(5), "Plang")
    def test_for_10(self):
        self.assertEqual(raindrops(10), "Plang")
    def test_for_25(self):
        self.assertEqual(raindrops(25), "Plang")
    def test_for_125(self):
        self.assertEqual(raindrops(125), "Plang")
    
    #Testing numbers with Factors of 7
    def test_for_7(self):
        self.assertEqual(raindrops(7), "Plong")
    def test_for_14(self):
        self.assertEqual(raindrops(14), "Plong")
    def test_for_49(self):
        self.assertEqual(raindrops(49), "Plong")
    def test_for_343(self):
        self.assertEqual(raindrops(343), "Plong")

    #Testing numbers with Factors of 3 & 5
    def test_for_15(self):
        self.assertEqual(raindrops(15), "PlingPlang")
    def test_for_30(self):
        self.assertEqual(raindrops(30), "PlingPlang")
    def test_for_225(self):
        self.assertEqual(raindrops(225), "PlingPlang")
    def test_for_3375(self):
        self.assertEqual(raindrops(3375), "PlingPlang")

    #Testing numbers with Factors of 5 & 7
    def test_for_35(self):
        self.assertEqual(raindrops(35), "PlangPlong")
    def test_for_70(self):
        self.assertEqual(raindrops(70), "PlangPlong")
    def test_for_1225(self):
        self.assertEqual(raindrops(1225), "PlangPlong")
    def test_for_42875(self):
        self.assertEqual(raindrops(42875), "PlangPlong")

    #Testing numbers with Factors of 3 & 7
    def test_for_21(self):
        self.assertEqual(raindrops(21), "PlingPlong")
    def test_for_42(self):
        self.assertEqual(raindrops(42), "PlingPlong")
    def test_for_441(self):
        self.assertEqual(raindrops(441), "PlingPlong")
    def test_for_9261(self):
        self.assertEqual(raindrops(9261), "PlingPlong")

    #Testing numbers with Factors of 3, 5, 7
    def test_for_105(self):
        self.assertEqual(raindrops(105), "PlingPlangPlong")
    def test_for_210(self):
        self.assertEqual(raindrops(210), "PlingPlangPlong")
    def test_for_11025(self):
        self.assertEqual(raindrops(11025), "PlingPlangPlong")
    def test_for_1157625(self):
        self.assertEqual(raindrops(1157625), "PlingPlangPlong")
    

    #Testing for numbers with No Factor of 3, 5, 7
    def test_for_1(self):
        self.assertEqual(raindrops(1), "1")
    def test_for_8(self):
        self.assertEqual(raindrops(8), "8")
    def test_for_52(self):
        self.assertEqual(raindrops(52), "52")

    #Testing for String input
    def testing_for_string(self):
        self.assertEqual(raindrops("String"), "Error!! Please enter a number")

if __name__ == "__main__":
    unittest.main()