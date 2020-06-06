from flask import Flask, request, jsonify
import logging
from models import ItemIdLookup
from storage import Storage
from configuration import CONFIG


from flask import Blueprint


logger = logging.getLogger()

storage = Storage(CONFIG['MYSQL_URL'],
                  CONFIG['MYSQL_USERNAME'],
                  CONFIG['MYSQL_PASSWORD'],
                  CONFIG['MYSQL_DATABASE'])



item_id_lookup_api = Blueprint('item_id_lookup_api', __name__)

'''
 item_id_lookup Table Requests
'''
# Get item id lookup by index
@item_id_lookup_api.route('/item_id_lookup/index/<int:index>')
def item_id_lookup_index(index=None):
    if index is None:
        return jsonify('item_id_lookup index not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `index`=%s' % (ItemIdLookup().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get item id lookup by first column
@item_id_lookup_api.route('/item_id_lookup/0/<int:index>')
def item_id_lookup_zero(index=None):
    if index is None:
        return jsonify('item_id_lookup zero not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `0`=%s' % (ItemIdLookup().table_name, index)
        return jsonify(storage.find_one_with_query(query))

# Get item id lookup by second column
@item_id_lookup_api.route('/item_id_lookup/1/<int:index>')
def item_id_lookup_one(index=None):
    if index is None:
        return jsonify('item_id_lookup one not implemented')
    else:
        query = 'SELECT * FROM `%s` WHERE `1`=%s' % (ItemIdLookup().table_name, index)
        return jsonify(storage.find_one_with_query(query))

