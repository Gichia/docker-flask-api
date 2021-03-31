"""
File for user class and methods

Classes
-------
    UserModel

Methods
-------
    json()

Misc Variables
--------------
    None
"""

from typing import Optional, Dict


class UserModel:
    """
    A class to represent user methods
    ...

    Attributes
    ----------
        email(str): The user's email
        username(str): The user's unique username
        phone(str) | Optional: The user's phone number

    Methods
    -------
        json() -> Dict:
            Returns the json representation of the user
    """

    def __init__(
        self,
        email: str,
        username: str,
        user_id: int = None,
        phone: Optional[str] = "",
        **kwargs
    ):
        """
        The init method for the user class.
        ...

        Attributes
        ----------
            email(str): The user's email
            username(str): The user's unique username
            phone(str) | Optional: The user's phone number

        Methods
        -------
            json() -> Dict:
                Returns the json representation of the user
        """

        self.email = email
        self.phone = phone
        self._kwargs = kwargs
        self.user_id = user_id
        self.username = username

        super(UserModel, self).__init__()

    def json(self) -> Dict:
        """
        Returns a json representation of the user object.

        Parameters
        ----------
            None

        Returns
        -------
            object: A JSON object of the UserModel class
        """

        return {
            "email": self.email,
            "phone": self.phone,
            "user_id": self.user_id,
            "username": self.username,
        }
