import unittest

from name import get_full_name


class NameTest(unittest.TestCase):
    def test_fullname(self):
        name = get_full_name('sobirjon', 'ergashev')
        self.assertEqual(name, 'Sobirjon Ergashev')
        
    def test_middle_name(self):
        name = get_full_name('sobirjon', 'nabijonovich', 'ergashev')
        self.assertEqual(name, 'Sobirjon Ergashev Nabijonovich')
    
unittest.main()
























