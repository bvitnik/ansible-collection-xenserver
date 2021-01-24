# -*- coding: utf-8 -*-
#
# Copyright: (c) 2019, Bojan Vitnik <bvitnik@mainstream.rs>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import os
import json
import copy


# Common cached fixture data loaded from files.
fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
fixture_data = {}


def load_fixture(file_name):
    """Loads and caches fixture data from files."""
    file_path = os.path.join(fixture_path, file_name)

    if file_path in fixture_data:
        return fixture_data[file_path]

    with open(file_path) as fixture:
        data = fixture.read()

    if file_path.endswith('.json'):
        data = json.loads(data)

    fixture_data[file_path] = data

    return data


def load_xenapi_db(file_name=None):
    """
    Loads a sample of XenAPI DB from file.
    """
    # We always use ansible-test-common-db.json as a base XenAPI DB sample.
    # Additional DB data is then loaded from file_name if specified.
    fake_xenapi_db_data = copy.deepcopy(load_fixture('ansible-test-common-db.json'))

    # If file_name for additional XenAPI DB data is passed, update base
    # XenAPI DB data down to a field level. Additional XenAPI DB data can
    # override base data at field level.
    if file_name:
        for xenapi_class in list(load_fixture(file_name).keys()):
            if xenapi_class not in fake_xenapi_db_data:
                fake_xenapi_db_data[xenapi_class] = copy.deepcopy(load_fixture(file_name)[xenapi_class])
            else:
                for obj_ref in list(load_fixture(file_name)[xenapi_class].keys()):
                    if obj_ref not in fake_xenapi_db_data[xenapi_class]:
                        fake_xenapi_db_data[xenapi_class][obj_ref] = copy.deepcopy(load_fixture(file_name)[xenapi_class][obj_ref])
                    else:
                        for field in list(load_fixture(file_name)[xenapi_class][obj_ref].keys()):
                            fake_xenapi_db_data[xenapi_class][obj_ref][field] = copy.deepcopy(load_fixture(file_name)[xenapi_class][obj_ref][field])

    return fake_xenapi_db_data
