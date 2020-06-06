from flask import Flask, request, jsonify
import logging
from models import ItemNameMap
from storage import Storage
from configuration import CONFIG


from flask import Blueprint


logger = logging.getLogger()

storage = Storage(CONFIG['MYSQL_URL'],
                  CONFIG['MYSQL_USERNAME'],
                  CONFIG['MYSQL_PASSWORD'],
                  CONFIG['MYSQL_DATABASE'])



item_name_map_api = Blueprint('item_name_map_api', __name__)

'''
 item_name_map Table Requests
'''
# Get item name map by index
@item_name_map_api.route('/item_name_map/index/<int:index>')
def item_name_map_index(index=None):
    if index is None:
        return jsonify('item_name_map index not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `index`=%s' % (ItemNameMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get item name map by appid column
@item_name_map_api.route('/item_name_map/appid/<int:index>')
def item_name_map_appid(index=None):
    if index is None:
        return jsonify('item_name_map appid not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `appid`=%s' % (ItemNameMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get item name map by gamename column
@item_name_map_api.route('/item_name_map/gamename/<string:index>')
def item_name_map_gamename(index=None):
    if index is None:
        return jsonify('item_name_map gamename not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `gamename`=%s' % (ItemNameMap().table_name, index)
        return jsonify(storage.find_one_with_query(query))
