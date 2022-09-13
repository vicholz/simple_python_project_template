import datetime
import logging
import logging.config
import os

PRIVATE_CLASS_CONSTANT = "THIS IS ONLY ACCESSIBLE FROM WITHIN THE CONTEXT OF THIS CLASS AND NOT FROM CLASS INSTANCE."

class Sample2(object):
    """Simple Class Template
    - This class prints 'Hello World {specified name}' with a timestamp.
    """
    CLASS_CONSTANT = "Hello," # Accessible via self.CLASS_CONSTANT and/or class_instance.CLASS_CONSTANT.


    def __init__(self, verbose:bool=False):
        """
        Class constructor.
            - Args:
                - verbose (bool): used to set logging level.
            - Returns:
                - None.
            - Raises:
                - None.
        """

        logging.config.fileConfig("logging.conf")
        logging.getLogger().setLevel(logging.DEBUG if os.environ.get("DEBUG") or verbose else logging.INFO)
    
    def _get_formatted_date(self, ts_format:str="%Y/%m/%d @ %H:%M:%S"):
        """
        Sample internal/private helper method to get a formatted datetime string.
            - Args:
                - format (string): desired datetime format.
            - Returns:
                - string: datetime.
            - Raises:
                - None.
        """
        now = datetime.datetime.now()
        return now.strftime(ts_format)

    def hello_name(self, name, ts_format:str="%Y/%m/%d @ %H:%M:%S",):
        """
        Returns 'Hello, {name}!' with datetime.
            - Args:
                - None.
            - Returns:
                - None.
            - Raises:
                - None.
        """

        datetime_str = self._get_formatted_date(ts_format)

        message = f"[{datetime_str}] {self.CLASS_CONSTANT} {name}!"
        logging.debug(message)
        return message
