from _mysql import OperationalError
from flask_testing import TestCase

from muffin_web.muffin import db, create_app
from muffin_web.muffin.models.users_model import UsersModel

__author__ = 'ife'


class testUserModel(TestCase):

    def create_app(self):
        return create_app('testing')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    #user model test
    def testCreateUser(self):
        db.create_all()
        if not UsersModel.query.first():
            usersModel = UsersModel()
            usersModel.email = 'test@example.com'
            usersModel.password = 'test123'
            # self.assertRaises(OperationalError, usersModel.create_user())
            usersModel.create_user()

        result = UsersModel.query.first()
        self.assertEqual(result.email, 'test@example.com')

