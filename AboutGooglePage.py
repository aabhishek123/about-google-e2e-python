import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Test.BaseTest import BaseTest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AboutGoogle(BaseTest):

    @classmethod
    def setUp(cls):
        url = None
        cls.driver.get(url)
        cls.driver.maximize_window()

    def test_execute(self):
        # Start of Code
        pass
        # End of Code



