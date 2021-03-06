# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import io
import json
import jsontableschema
from . import base


class TestValidateSchema(base.BaseTestCase):

    def test_schema_valid_simple(self):
        filepath = os.path.join(self.data_dir, 'schema_valid_simple.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        valid = jsontableschema.validate(schema)
        self.assertTrue(valid)

    def test_schema_valid_full(self):
        filepath = os.path.join(self.data_dir, 'schema_valid_full.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        valid = jsontableschema.validate(schema)
        self.assertTrue(valid)

    def test_schema_valid_pk_string(self):
        filepath = os.path.join(self.data_dir, 'schema_valid_pk_string.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        valid = jsontableschema.validate(schema)
        self.assertTrue(valid)

    def test_schema_valid_pk_array(self):
        filepath = os.path.join(self.data_dir, 'schema_valid_pk_array.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        valid = jsontableschema.validate(schema)
        self.assertTrue(valid)

    def test_schema_invalid_empty(self):
        filepath = os.path.join(self.data_dir, 'schema_invalid_empty.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_invalid_wrong_type(self):
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_wrong_type.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_invalid_pk_string(self):
        filepath = os.path.join(self.data_dir, 'schema_invalid_pk_string.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_invalid_pk_array(self):
        filepath = os.path.join(self.data_dir, 'schema_invalid_pk_array.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_valid_fk_string(self):
        filepath = os.path.join(self.data_dir, 'schema_valid_fk_string.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        valid = jsontableschema.validate(schema)
        self.assertTrue(valid)

    def test_schema_valid_fk_string_self_ref(self):
        filepath = os.path.join(self.data_dir,
                                'schema_valid_fk_string_self_referencing.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        valid = jsontableschema.validate(schema)
        self.assertTrue(valid)

    def test_schema_valid_fk_array(self):
        filepath = os.path.join(self.data_dir,
                                'schema_valid_fk_array.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        valid = jsontableschema.validate(schema)
        self.assertTrue(valid)

    def test_schema_invalid_fk_string(self):
        filepath = os.path.join(self.data_dir, 'schema_invalid_fk_string.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_invalid_fk_no_reference(self):
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_fk_no_reference.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_invalid_fk_array(self):
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_fk_array.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_invalid_fk_ref_is_an_array_fields_is_a_string(self):
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_fk_string_array_ref.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_invalid_fk_reference_is_a_string_fields_is_an_array(self):
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_fk_array_string_ref.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_schema_invalid_fk_reference_array_number_mismatch(self):
        '''the number of foreignKey.fields is not the same as

        'foreignKey.reference.fields'
        '''
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_fk_array_wrong_number.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
        self.assertRaises(jsontableschema.exceptions.SchemaValidationError,
                          jsontableschema.validate,
                          schema)

    def test_primary_key_is_not_a_valid_type(self):
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_pk_is_wrong_type.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
            errors = [i for i in jsontableschema.validator.iter_errors(schema)]
        self.assertEquals(2, len(errors))



class TestValidator(base.BaseTestCase):
    def test_schema_multiple_errors(self):
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_multiple_errors.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
            errors = [i for i in jsontableschema.validator.iter_errors(schema)]
        self.assertEquals(5, len(errors))

    def test_schema_no_fields(self):
        filepath = os.path.join(self.data_dir,
                                'schema_invalid_pk_no_fields.json')
        with io.open(filepath) as stream:
            schema = json.load(stream)
            errors = [i for i in jsontableschema.validator.iter_errors(schema)]
        self.assertEquals(3, len(errors))
