# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 21:23:35 2022

@author: ObiraDaniel
"""
import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    """Unit test cases for English and French translation"""
    def test_englishtoFrench1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_englishtoFrench2(self):
        self.assertNotEqual(englishToFrench("Hello"), "Welcome")

    def test_frenchToEnglish1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_frenchToEnglish2(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Testing")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
