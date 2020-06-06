from flask import Flask, request, jsonify
import logging
from models import UserBundleMap
from storage import Storage
from configuration import CONFIG


from flask import Blueprint


logger = logging.getLogger()

storage = Storage(CONFIG['MYSQL_URL'],
                  CONFIG['MYSQL_USERNAME'],
                  CONFIG['MYSQL_PASSWORD'],
                  CONFIG['MYSQL_DATABASE'])



user_bundle_map_api = Blueprint('user_bundle_map_api', __name__)


'''
 user_bundle_map Table Requests
'''
# Get user bundle map by index
@user_bundle_map_api.route('/user_bundle_map/index/<int:index>')
def user_bundle_map_index(index=None):
    if index is None:
        return jsonify('user_bundle_map index not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `index`=%s' % (UserBundleMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get user bundle map by first column
@user_bundle_map_api.route('/user_bundle_map/0/<int:index>')
def user_bundle_map_zero(index=None):
    if index is None:
        return jsonify('user_bundle_map zero not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `0`=%s' % (UserBundleMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get user bundle map by second column
@user_bundle_map_api.route('/user_bundle_map/1/<int:index>')
def user_bundle_map_one(index=None):
    if index is None:
        return jsonify('user_bundle_map one not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `1`=%s' % (UserBundleMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))
