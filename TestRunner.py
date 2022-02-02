import os
import unittest
import datetime
import HtmlTestRunner
from pathlib import Path

from Test.AboutGooglePage import AboutGoogle

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromTestCase(AboutGoogle))

dir_path = os.getcwd()

timestamp_for_file = '{date:%Y-%m-%d_%H-%M-%S}'.format(date = datetime.datetime.now())

temp_data_dir = "runs/"

outfile = open(dir_path + '/' + temp_data_dir + "TestConsole_" + timestamp_for_file + ".log", "w")
# 
runner = HtmlTestRunner.HTMLTestRunner(stream =outfile, combine_reports = True, report_name='TestRunner')

results = runner.run(suite)
