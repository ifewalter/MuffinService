from flask_testing import TestCase

from muffin_web.muffin import db, create_app
from muffin_web.muffin.models import users_model, DomainsModel

__author__ = 'ife'


class testDomainsModel(TestCase):

    def create_app(self):
        return create_app('testing')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    #test domains
    def testDomains(self):
        if not DomainsModel.query.first():
            domainsModel = DomainsModel()

            domainsModel.url = 'http://example.com/'
            domainsModel.name = 'Example'
            domainsModel.save()

            result = domainsModel.query.first()
            self.assertEqual(result.name, 'Example')



        
