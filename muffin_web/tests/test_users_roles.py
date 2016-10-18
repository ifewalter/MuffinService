from flask_testing import TestCase

from muffin_web.manage import user_datastore
from muffin_web.muffin import db, create_app
from muffin_web.muffin.models import users_model

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
        if not users_model.query.first():
            user_datastore.create_user(email='test@example.com', password='test123')
            db.session.commit()
        result = users_model.query.first()
        self.assertEqual(result.email, 'test@example.com')
