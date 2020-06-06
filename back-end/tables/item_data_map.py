from flask import Flask, request, jsonify
import logging
from models import ItemDataMap
from storage import Storage
from configuration import CONFIG


from flask import Blueprint


logger = logging.getLogger()

storage = Storage(CONFIG['MYSQL_URL'],
                  CONFIG['MYSQL_USERNAME'],
                  CONFIG['MYSQL_PASSWORD'],
                  CONFIG['MYSQL_DATABASE'])



item_data_map_api = Blueprint('item_data_map_api', __name__)

'''
 item_data_map Table Requests
'''
# Get item data map by index
@item_data_map_api.route('/item_data_map/index/<int:index>')
def item_data_map_index(index=None):
    if index is None:
        return jsonify('item_data_map index not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `index`=%s' % (ItemDataMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get item data map by appid
@item_data_map_api.route('/item_data_map/appid/<string:appid>')
def item_data_map_appid(appid=None):
    if appid is None:
        return jsonify('item_data_map appid not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE appid=%s' % (ItemDataMap().table_name, appid)
        return jsonify(storage.find_one_with_query(query))
