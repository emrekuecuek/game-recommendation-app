from flask import Flask, request, jsonify
import logging
from models import BundleItemMap
from storage import Storage
from configuration import CONFIG


from flask import Blueprint


logger = logging.getLogger()

storage = Storage(CONFIG['MYSQL_URL'],
                  CONFIG['MYSQL_USERNAME'],
                  CONFIG['MYSQL_PASSWORD'],
                  CONFIG['MYSQL_DATABASE'])



bundle_item_map_api = Blueprint('bundle_item_map_api', __name__)


'''
 bundle_item_map Table Requests
'''
# Get bundle item map by index
@bundle_item_map_api.route('/bundle_item_map/index/<int:index>')
def bundle_item_map_index(index=None):
    if index is None:
        return jsonify('bundle_item_map index not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `index`=%s' % (BundleItemMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get bundle item map by first column
@bundle_item_map_api.route('/bundle_item_map/0/<int:index>')
def bundle_item_map_zero(index=None):
    if index is None:
        return jsonify('bundle_item_map zero not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `0`=%s' % (BundleItemMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get bundle item map by second column
@bundle_item_map_api.route('/bundle_item_map/1/<int:index>')
def bundle_item_map_one(index=None):
    if index is None:
        return jsonify('bundle_item_map one not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `1`=%s' % (BundleItemMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

