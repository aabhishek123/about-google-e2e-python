import unittest

from selenium import webdriver

class BaseTest(unittest.TestCase):

    path = None
    driver = webdriver.Chrome(path)