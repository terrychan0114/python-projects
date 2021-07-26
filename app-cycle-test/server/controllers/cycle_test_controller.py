import connexion
import six

from server.models.cycle_test_info import CycleTestInfo  # noqa: E501
from server import util


def add_info(body):  # noqa: E501
    """Add a new info to the server

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CycleTestInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_info():  # noqa: E501
    """Get the information

     # noqa: E501


    :rtype: List[CycleTestInfo]
    """
    return 'do some magic!'
