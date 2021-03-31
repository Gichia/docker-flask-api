from app.models.users.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):

    def test_crud(self):
        with self.app_context():

            user = UserModel(email="testemail", username="test")

            self.assertIsNone(UserModel.find_by_username(username="test"))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username(username="test"))

            user.delete_from_db()

            self.assertIsNone(UserModel.find_by_username(username="test"))
