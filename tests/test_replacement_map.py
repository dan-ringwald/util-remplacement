from os.path import dirname, abspath, join
from util_replacement import ReplacementMap
import unittest

class TestReplacementMap(unittest.TestCase):
    def test_replacement(self):
        d = dirname(dirname(abspath(__file__)))
        d = join(d, 'assets', 'config_example.yaml')
        replacement_map = ReplacementMap(d)
        replaced = replacement_map.process_text('( test??)')
        self.assertEqual(replaced, '(test?)')

if __name__ == '__main__':
    unittest.main()
