from flask import Flask, request, jsonify
import logging
from models import UserItemMap
from storage import Storage
from configuration import CONFIG


from flask import Blueprint


logger = logging.getLogger()

storage = Storage(CONFIG['MYSQL_URL'],
                  CONFIG['MYSQL_USERNAME'],
                  CONFIG['MYSQL_PASSWORD'],
                  CONFIG['MYSQL_DATABASE'])



user_item_map_api = Blueprint('user_item_map_api', __name__)


'''
 user_item_map Table Requests
'''
# Get user item map by index
@user_item_map_api.route('/user_item_map/index/<int:index>')
def user_item_map_index(index=None):
    if index is None:
        return jsonify('user_item_map index not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `index`=%s' % (UserItemMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get user item map by first column
@user_item_map_api.route('/user_item_map/0/<int:index>')
def user_item_map_zero(index=None):
    if index is None:
        return jsonify('user_item_map zero not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `0`=%s' % (UserItemMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get user item map by second column
@user_item_map_api.route('/user_item_map/1/<int:index>')
def user_item_map_one(index=None):
    if index is None:
        return jsonify('user_item_map one not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `1`=%s' % (UserItemMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))
