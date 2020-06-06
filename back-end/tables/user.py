from flask import Flask, request, jsonify
import logging
from models import User
from storage import Storage
from configuration import CONFIG


from flask import Blueprint


logger = logging.getLogger()

storage = Storage(CONFIG['MYSQL_URL'],
                  CONFIG['MYSQL_USERNAME'],
                  CONFIG['MYSQL_PASSWORD'],
                  CONFIG['MYSQL_DATABASE'])



user_api = Blueprint('user_api', __name__)

'''
 User Table Requests
'''
# Get user by customer id
@user_api.route('/user/<string:customer_id>')
def user(customer_id=None):
    if customer_id is None:
        return jsonify('multiple user not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE customer_id=%s' % (User().table_name, customer_id)
        return jsonify(storage.find_one_with_query(query))
