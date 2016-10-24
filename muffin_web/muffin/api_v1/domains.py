from flask import jsonify, request

from . import api
from .. import db
from rest_framework import status


@api.route('/domains', methods=['POST'])
def create_domain():
    pass
