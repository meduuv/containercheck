import unittest
from containercheck import validate

class ContainerCheckTests(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate([{"name":"api","image":"python"}]), [])
    def test_invalid(self): self.assertEqual(validate([{}]), ["container[0]: missing name", "container[0]: missing image"])

if __name__ == "__main__": unittest.main()
