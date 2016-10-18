from flask_testing import TestCase

from MuffinWeb.manage import user_datastore
from MuffinWeb.muffin import db, create_app
from MuffinWeb.muffin.models import UsersModel

__author__ = 'ife'


class testUserRoles(TestCase):

    def create_app(self):
        return create_app('testing')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def testCreateUser(self):
        db.create_all()
        if not UsersModel.query.first():
            user_datastore.create_user(email='test@example.com', password='test123')
            db.session.commit()
        result = UsersModel.query.first()
        self.assertEqual(result.email, 'test@example.com')
