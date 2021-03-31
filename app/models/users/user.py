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

from typing import Optional, Dict, List, Union

from main import db


class UserModel(db.Model):
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

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=False, nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(
        self,
        email: str,
        username: str,
        id: int = None,
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

        self.id = id
        self.email = email
        self.phone = phone
        self._kwargs = kwargs
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
            "id": self.id,
            "email": self.email,
            "phone": self.phone,
            "username": self.username,
        }

    @classmethod
    def find_by_username(
        cls,
        username: str
    ) -> Union[List, None]:
        """

        """

        return cls.query.filter_by(username=username).first()

    def save_to_db(self):
        """
        
        """

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        
        """

        db.session.delete(self)
        db.session.commit()
