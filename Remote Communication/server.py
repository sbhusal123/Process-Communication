from multiprocessing.managers import BaseManager

import logging

logger = logging.getLogger(__name__)

data_items = {}

def get_item(key):
    global data_items
    logger.info(f"Getting a dataitem: key = {key}")
    if key in data_items.keys():
        return data_items[key]
    return None

def add_item(key, data):
    global data_items
    logger.info(f"Adding a dataitem: key = {key} , data={data}")
    data_items[key] = data



if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 3456
    PASSWORD = b'password'
    manager = BaseManager((HOST, PORT), PASSWORD)
    manager.register('get_item', get_item)
    manager.register('add_item', add_item)
    server = manager.get_server()
    print(f"Process server starting on: {HOST}:{PORT}")
    server.serve_forever()
