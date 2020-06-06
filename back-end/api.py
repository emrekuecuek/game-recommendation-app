from flask import Flask, request, jsonify
import logging
# from models import User, BundleItemMap, ItemDataMap, ItemIdLookup, ItemNameMap, UserBundleMap, UserItemMap
from storage import Storage
from configuration import CONFIG
from tables.user_item_map import user_item_map_api
from tables.user_bundle_map import user_bundle_map_api
from tables.item_name_map import item_name_map_api
from tables.item_id_lookup import item_id_lookup_api
from tables.item_data_map import item_data_map_api
from tables.bundle_item_map import bundle_item_map_api
from tables.user import user_api

import json
count = 0
global_results = []


logger = logging.getLogger()
app = Flask(__name__)
storage = Storage(CONFIG['MYSQL_URL'],
                  CONFIG['MYSQL_USERNAME'],
                  CONFIG['MYSQL_PASSWORD'],
                  CONFIG['MYSQL_DATABASE'])


app.register_blueprint(user_item_map_api)
app.register_blueprint(user_bundle_map_api)
app.register_blueprint(item_name_map_api)
app.register_blueprint(item_id_lookup_api)
app.register_blueprint(item_data_map_api)
app.register_blueprint(bundle_item_map_api)
app.register_blueprint(user_api)

@app.route('/')
def api_map():
    links = []
    for rule in app.url_map.iter_rules():
        links.append('%s' % rule.rule)
    return jsonify(links)


@app.route('/userinfo/<int:userid>/<string:gamename>')
def userinfo(userid=None, gamename=None):
    if userid is None or gamename is None:
        return jsonify("userinfo not implemented")
    else:
        data = {"userid":userid,"gamename": gamename}
        return jsonify(data)

@app.route('/sendbasketinfo', methods=['GET','POST'])
def sendbasketinfo():
    if request.method == 'GET':
        return jsonify("This function needs POST as return")
    elif request.method == 'POST':
        basket_list = request.form
        return basket_list
    else:
        return jsonify("HTTP header neither GET nor POST")


@app.route('/test')
def test():
    return Storage('localhost', 'djangouser', 'password', 'steamdb').test()


import json
count = 0
global_results = []
app = Flask(__name__)
@app.route('/abd', methods=['GET', 'POST'])
def abd():

    data1 = request.json
    data_col = set()
    data2 = json.loads(json.dumps(data1))
    data3 = jsonify(data1)
    if data1 is not None:
        for itr in data1:
            data_col.add(get_key(get_key(itr['name'], bundle_generator.item_name_map), bundle_generator.item_id_lookup))
        bundle_generator.bundle_item_map.update({max(bundle_generator.bundle_item_map) + 1 : data_col})
        if 'count' not in locals():
            count = 0
        if count == 0:
            bundle_generator.user_bundle_map.update({max(bundle_generator.user_bundle_map) +1 : {max(bundle_generator.bundle_item_map)}})
        else:
            bundle_generator.user_bundle_map[max(bundle_generator.user_bundle_map)].add(max(bundle_generator.bundle_item_map))
    
        for i in bundle_generator.bundle_item_map[max(bundle_generator.bundle_item_map)]:
            bundle_generator.user_item_map[max(bundle_generator.user_bundle_map)].add(i)                                                                            
                                                                                    
        bundle_generator.bpr_item = bundle_generator.BPR_Item(10, len(bundle_generator.user_item_map.keys()), len(bundle_generator.items_set))
        bundle_generator.bpr_cold = bundle_generator.BPR_Cold(10, bundle_generator.max_bundle_size, len(bundle_generator.user_bundle_map.keys()), len(bundle_generator.items_set))
        bundle_result = bundle_generator.generate_bundle(bundle_generator.items_set, max(bundle_generator.user_bundle_map), 4, 1000,10)
        to_send = []                                                                                
        for res in bundle_result:
            to_send.append(bundle_generator.item_name_map[bundle_generator.item_id_lookup[res]])  
                                                                                   
    print(type(data2))
    
    if 'count'  in locals():
        count = count + 1
    print(data_col)
    
    
    if 'to_send' not in locals():
        return jsonify({'gamename': ['Team Fortress Classic','Naruto Shippuden Uncut: Guardian of the Iron Wall','Mad Max Beyond Thunderdome' ]})
    else:
        
        
        print(to_send)
        #return jsonify({'gamename': 1})
        global_results.append(to_send)
        return jsonify({'gamename': global_results[len(global_results)-1]})
@app.route('/abc', methods=['GET','POST'])
def abc():
    return "Hello"


@app.route('/resres', methods=['GET','POST'])
def resres():
    if len(global_results)>0:
        return jsonify({'gamename': global_results[len(global_results)-1]})
    else:
        return jsonify({'gamename': ['Team Fortress Classic','Naruto Shippuden Uncut: Guardian of the Iron Wall','Mad Max Beyond Thunderdome' ]})

if __name__ == '__main__':
    app.debug = True
    app.run()
