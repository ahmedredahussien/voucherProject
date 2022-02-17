# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Segment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, frequent_segment: str=None, recency_segment: str=None):  # noqa: E501
        """Segment - a model defined in Swagger

        :param frequent_segment: The frequent_segment of this Segment.  # noqa: E501
        :type frequent_segment: str
        :param recency_segment: The recency_segment of this Segment.  # noqa: E501
        :type recency_segment: str
        """
        self.swagger_types = {
            'frequent_segment': str,
            'recency_segment': str
        }

        self.attribute_map = {
            'frequent_segment': 'frequent_segment',
            'recency_segment': 'recency_segment'
        }
        self._frequent_segment = frequent_segment
        self._recency_segment = recency_segment

    @classmethod
    def from_dict(cls, dikt) -> 'Segment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Segment of this Segment.  # noqa: E501
        :rtype: Segment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def frequent_segment(self) -> str:
        """Gets the frequent_segment of this Segment.

        number of orders for customer  # noqa: E501

        :return: The frequent_segment of this Segment.
        :rtype: str
        """
        return self._frequent_segment

    @frequent_segment.setter
    def frequent_segment(self, frequent_segment: str):
        """Sets the frequent_segment of this Segment.

        number of orders for customer  # noqa: E501

        :param frequent_segment: The frequent_segment of this Segment.
        :type frequent_segment: str
        """
        allowed_values = ["0-4", "5-13", "13-37"]  # noqa: E501
        if frequent_segment not in allowed_values:
            raise ValueError(
                "Invalid value for `frequent_segment` ({0}), must be one of {1}"
                .format(frequent_segment, allowed_values)
            )

        self._frequent_segment = frequent_segment

    @property
    def recency_segment(self) -> str:
        """Gets the recency_segment of this Segment.

        days since last customer order by a customer  # noqa: E501

        :return: The recency_segment of this Segment.
        :rtype: str
        """
        return self._recency_segment

    @recency_segment.setter
    def recency_segment(self, recency_segment: str):
        """Sets the recency_segment of this Segment.

        days since last customer order by a customer  # noqa: E501

        :param recency_segment: The recency_segment of this Segment.
        :type recency_segment: str
        """
        allowed_values = ["30-60", "60-90", "90-120", "120-180", "180+"]  # noqa: E501
        if recency_segment not in allowed_values:
            raise ValueError(
                "Invalid value for `recency_segment` ({0}), must be one of {1}"
                .format(recency_segment, allowed_values)
            )

        self._recency_segment = recency_segment
