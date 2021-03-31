"""
BaseTest

This class should be parent class for each non-unit test.
It allows for the instantiation of the database dynamically
and makes sure that it is a new , blank database each time.
"""

import os
from unittest import TestCase
from main import app, db
# from db import db


class BaseTest(TestCase):

    def setUp(self):
        """
        Makes sure database exists
        Get a test client
        """

        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("TEST_DB_URI")

        with app.app_context():
            db.init_app(app=app)
            db.create_all()

        # Get test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        """
        Ensures database is blank
        """

        with app.app_context():
            db.session.remove()
            db.drop_all()
