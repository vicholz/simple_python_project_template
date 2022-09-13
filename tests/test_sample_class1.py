
import datetime
import unittest

from simple_python_project_template.sample_class1 import Sample1


DEFAULT_MESSAGE = "Hello World!"
DEFAULT_TS_FORMAT = "%Y/%m/%d @ %H:%M:%S"
TEST_TS_FORMAT = "%Y"


class TestCases(unittest.TestCase):
    def test_get_formatted_date(self):
        """
        Test default timestamp format.
        """
        # create an instance of the Sample1 class.
        cls = Sample1()
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
        cls = Sample1()
        # get a timestamp string using the class method _get_formatted_date.
        cls_ts = cls._get_formatted_date(TEST_TS_FORMAT)

        # get the current time
        now = datetime.datetime.now()
        # get the current timestamp
        now_ts = now.strftime(TEST_TS_FORMAT)

        # check to make sure they are similar format.
        self.assertAlmostEqual(cls_ts, now_ts)

    def test_hello_world(self):
        """
        Test hello_world method.
        """

        # create an instance of the Sample1 class.
        cls = Sample1()
        # get a timestamp string using the class method _get_formatted_date.
        rtn = cls.hello_world()

        # get the current time
        now = datetime.datetime.now()
        # get the current timestamp
        now_ts = now.strftime(DEFAULT_TS_FORMAT)
        # create message string
        message = f"[{now_ts}] {DEFAULT_MESSAGE}"

        # check to make sure they are similar format.
        self.assertAlmostEqual(rtn, message)
