#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from pandoras_flask import app


class TestPandorasFlask(unittest.TestCase):

    def setUp(self):
        self.client = app.ping_app.test_client()

        # Ensure metrics are initialized by making a call prior to tests.
        self.client.get('/ping')

    def tearDown(self):
        pass

    def test_ping(self):
        rp = self.client.get('/ping')
        self.assertEqual(rp.status_code, 200)
        self.assertEqual(rp.get_data(), 'Pong')

    def test_metrics(self):
        rp = self.client.get('/metrics')
        self.assertEqual(rp.status_code, 200)
        self.assertIn('request_count_total', rp.get_data())
