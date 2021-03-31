from unittest import TestCase

from users.user import UserModel


class UserTest(TestCase):
    """
    A class to implement unit tests for user objects

    ...

    Attributes
    ----------
    None

    Methods
    -------
        test_create_user() -> None
        test_user_json() -> None
        test_create_superuser() -> None
    """

    def test_create_user(self):
        """
        Tests the creation of user object.
        """

        user = UserModel(
                    email="jdoe@test.com",
                    username="testuser",
                    password="@testpass123!",
                    status=1)

        self.assertEqual(
            user.email,
            "jdoe@test.com",
            "The email of the user after creation does not equal the constructor arguement."
        )
        self.assertEqual(
            user.username,
            "testuser",
            "The username of the user after creation does not equal the constructor arguement."
        )

    def test_user_json(self):
        """
        Tests the creation of user JSON object.
        """

        user = UserModel(
                    first_name="John",
                    email="jdoe@test.com",
                    username="testuser",
                    password="@testpass123!")

        excepted = {
            "phone": "",
            "user_id": None,
            "username": "testuser",
            "email": "jdoe@test.com",
        }

        self.assertDictEqual(
            user.json(),
            excepted,
            "The JSON export is incorrect. Expected {} but recieved {}".format(excepted, user.json())
        )
