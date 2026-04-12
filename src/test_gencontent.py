import unittest
import re
from gencontent import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_gen_md(self):
        markdown = extract_title(
            "# My Adventure Log\n## Day One\nToday I found a **magical cave**."
        )
        self.assertEqual("My Adventure Log", markdown)