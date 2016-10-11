
from muffinAPI.models.UserModel import UserModel

__author__ = 'ife'


class UserService:

    def create_user(self, username, password, email, token, user_id, provider, device_id):
        userModel = UserModel(username, password, email, token, user_id, provider, device_id)
        userModel.add(userModel)

    def get_by_username(self, username):
        userModel = UserModel()
        userModel.get
