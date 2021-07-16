import unittest
import sentenceValidator as sv


class TestStringMethods(unittest.TestCase):

    # these unit tests form the basis of the valid given sentences from the examples

    def test_valid1(self):
        result = sv.sentence_builder("The quick brown fox said “hello Mr lazy dog”.")
        self.assertTrue(result)

    def test_isValid2(self):
        result = sv.sentence_builder("The quick brown fox said hello Mr lazy dog.")
        self.assertTrue(result)

    def test_numIsValid(self):
        result = sv.sentence_builder("One lazy dog is too few, 13 is too many.")
        self.assertTrue(result)

    def test_numWordIsValid(self):
        result = sv.sentence_builder("One lazy dog is too few, thirteen is too many.")
        self.assertTrue(result)

    def test_lastCharNotPeriod(self):
        result = sv.sentence_builder('The quick brown fox said "hello Mr. lazy dog".')
        self.assertFalse(result)

    def test_lowerCaseFirstLetter(self):
        result = sv.sentence_builder('the quick brown fox said “hello Mr lazy dog".')
        self.assertFalse(result)

    def test_unbalancedParenthesis(self):
        result = sv.sentence_builder('"The quick brown fox said “hello Mr lazy dog."')
        self.assertFalse(result)

    def test_numberWordNotValid(self):
        result = sv.sentence_builder('One lazy dog is too few, 12 is too many.')
        self.assertFalse(result)

    def test_numberWordNotValid(self):
        result = sv.sentence_builder('One lazy dog is too few, 12 is too many.')
        self.assertFalse(result)

    # additional unit tests to test other cases

    def test_multipleNums(self):
        result = sv.sentence_builder('Numbers 1, 19, 29 and 27.')
        self.assertFalse(result)

    def test_multipleNumsWords(self):
        result = sv.sentence_builder('Numbers one, ten, 29 and 27.')
        self.assertTrue(result)

    def test_multipleParenthesis(self):
        result = sv.sentence_builder('I heard him say, "Ok"; then she said, "What?!".')
        self.assertTrue(result)

    def test_sentenceStartsWithNumber(self):
        result = sv.sentence_builder('101 dalmations is a 1996 Disney film.')
        self.assertFalse(result)

    def test_sentenceEndsWithInvalidChar(self):
        result = sv.sentence_builder('How are you doing?')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
