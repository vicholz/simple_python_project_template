
import datetime
import unittest
from simple_python_project_template.sample_class2 import Sample2

DEFAULT_NAME = "FOO"
DEFAULT_MESSAGE = f"Hello, {DEFAULT_NAME}!"
DEFAULT_TS_FORMAT = "%Y/%m/%d @ %H:%M:%S"
TEST_TS_FORMAT = "%Y"


class TestCases(unittest.TestCase):
    def test_get_formatted_date(self):
        """
        Test default timestamp format.
        """
        # create an instance of the Sample1 class.
        cls = Sample2()
        # get a timestamp string using the class method _get_formatted_date.
        cls_ts = cls._get_formatted_date()

        # get the current time
        now = datetime.datetime.now()
        # get the current timestamp
        now_ts = now.strftime(DEFAULT_TS_FORMAT)

        # check to make sure they are similar format.
        self.assertAlmostEqual(cls_ts, now_ts)

    def test_get_formatted_date_alternate_format(self):
        """
        Test non-default timestamp format.
        """

        # create an instance of the Sample1 class.
        cls = Sample2()
        # get a timestamp string using the class method _get_formatted_date.
        cls_ts = cls._get_formatted_date(TEST_TS_FORMAT)

        # get the current time
        now = datetime.datetime.now()
        # get the current timestamp
        now_ts = now.strftime(TEST_TS_FORMAT)

        # check to make sure they are similar format.
        self.assertAlmostEqual(cls_ts, now_ts)

    def test_hello_name(self):
        """
        Test hello_world method.
        """

        # create an instance of the Sample1 class.
        cls = Sample2()
        # get a timestamp string using the class method _get_formatted_date.
        rtn = cls.hello_name(DEFAULT_NAME)

        # get the current time
        now = datetime.datetime.now()
        # get the current timestamp
        now_ts = now.strftime(DEFAULT_TS_FORMAT)
        # create message string
        message = f"[{now_ts}] {DEFAULT_MESSAGE}"

        # check to make sure they are similar format.
        self.assertAlmostEqual(rtn, message)
