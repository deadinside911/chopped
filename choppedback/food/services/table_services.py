import secrets
import string

from food.models import Table

JOIN_CODE_LENGTH = 6

class TableService():
    """
    """

    @staticmethod
    def _generate_join_code() -> str:
        """"""
        return "".join([secrets.choice(string.ascii_uppercase + string.digits) for _ in range(JOIN_CODE_LENGTH)])

    @staticmethod
    def create_table():
        """"""
        pass
