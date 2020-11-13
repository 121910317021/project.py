def prefix_words(prefix, words):
    first=[]
    for word in words:
        if word.startswith(prefix):
            first.append(word)
    return first


class TestPrefixWords(unittest.TestCase):

    def test_1(self):
        self.assertEqual(prefix_words(
            'de', ['dog', 'deal', 'deer']), ['deal', 'deer'])

    def test_2(self):
        self.assertEqual(prefix_words(
            'b', ['banana', 'binary', 'carrot', 'bit', 'boar']), ['banana', 'binary', 'bit', 'boar'])


if __name__ == '__main__':
    unittest.main(verbosity=2)