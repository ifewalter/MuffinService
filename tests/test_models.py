# -*- coding: utf-8 -*-
from muffinAPI.models.UserModel import UserModel

from tests import TestCase


class TestUser(TestCase):

    def test_get_current_time(self):

        assert UserModel.query.count() == 2
        # assert UserDetail.query.count() == 2
