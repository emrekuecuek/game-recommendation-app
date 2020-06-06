class Model(object):
    pass


class User(Model):
    def __init__(self):
        self.table_name = 'steam_user'

class BundleItemMap(Model):
	def __init__(self):
		self.table_name = 'bundle_item_map'

class ItemDataMap(Model):
	def __init__(self):
		self.table_name = 'item_data_map'

class ItemIdLookup(Model):
	def __init__(self):
		self.table_name = 'item_id_lookup'

class ItemNameMap(Model):
	def __init__(self):
		self.table_name = 'item_name_map'

class UserBundleMap(Model):
	def __init__(self):
		self.table_name = 'user_bundle_map'

class UserItemMap(Model):
	def __init__(self):
		self.table_name = 'user_item_map'

# class TransactionStory(Model):
#     def __init__(self):
#         self.table_name = 'groceryapi_transactionstory'


# class Product(Model):
#     def __init__(self):
#         self.table_name = 'groceryapi_product'
