# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.model.required_with_empty_array import RequiredWithEmptyArray
from unit_test_api import configuration


class TestRequiredWithEmptyArray(unittest.TestCase):
    """RequiredWithEmptyArray unit test stubs"""
    _configuration = configuration.Configuration()

    def test_property_not_required_passes(self):
        # property not required
        RequiredWithEmptyArray._from_openapi_data(
            {
            },
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
