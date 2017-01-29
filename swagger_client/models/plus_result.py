# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class PlusResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, operator_a=None, operator_b=None, result=None):
        """
        PlusResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'operator_a': 'int',
            'operator_b': 'int',
            'result': 'int'
        }

        self.attribute_map = {
            'operator_a': 'operatorA',
            'operator_b': 'operatorB',
            'result': 'result'
        }

        self._operator_a = operator_a
        self._operator_b = operator_b
        self._result = result

    @property
    def operator_a(self):
        """
        Gets the operator_a of this PlusResult.


        :return: The operator_a of this PlusResult.
        :rtype: int
        """
        return self._operator_a

    @operator_a.setter
    def operator_a(self, operator_a):
        """
        Sets the operator_a of this PlusResult.


        :param operator_a: The operator_a of this PlusResult.
        :type: int
        """

        self._operator_a = operator_a

    @property
    def operator_b(self):
        """
        Gets the operator_b of this PlusResult.


        :return: The operator_b of this PlusResult.
        :rtype: int
        """
        return self._operator_b

    @operator_b.setter
    def operator_b(self, operator_b):
        """
        Sets the operator_b of this PlusResult.


        :param operator_b: The operator_b of this PlusResult.
        :type: int
        """

        self._operator_b = operator_b

    @property
    def result(self):
        """
        Gets the result of this PlusResult.


        :return: The result of this PlusResult.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this PlusResult.


        :param result: The result of this PlusResult.
        :type: int
        """

        self._result = result

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other