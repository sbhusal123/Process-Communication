# Remote Process Communication

What we are basically doing is communicating with a remote process over a network.

[Reference Here](https://docs.python.org/3/library/multiprocessing.html#managers)

More speciallt we are using a [BaseManager](https://docs.python.org/3/library/multiprocessing.html#customized-managers)


## Server:

```python
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
    HOST = 'localhost'
    PORT = 3456
    PASSWORD = b'password'
    manager = BaseManager((HOST, PORT), PASSWORD)
    manager.register('get_item', get_item)
    manager.register('add_item', add_item)
    server = manager.get_server()
    print(f"Process server starting on: {HOST}:{PORT}")
    server.serve_forever()

```

Here, server manager exposes two methods ``get_item`` and ``set_item`` on the specified HOST so that client can access those.


## Client 1

```python
from multiprocessing.managers import BaseManager


HOST = 'localhost'
PORT = 3456
PASSWORD = b'password'

manager = BaseManager((HOST, PORT), PASSWORD)

manager.register('get_item')
manager.register('add_item')
manager.connect()

manager.add_item("user", {
    "name": "surya bhusal", 
    "email": "test@gmail.com"
})

```

What we're doing here is, connecting to the server on host and port, basically through this client we're adding am item with key and value to the dictionary on server.

Similarly, we can also access it through the another client as:

```python
from multiprocessing.managers import BaseManager


HOST = 'localhost'
PORT = 3456
PASSWORD = b'password'

manager = BaseManager((HOST, PORT), PASSWORD)

manager.register('get_item')
manager.connect()

item = manager.get_item("user")

print(item)

```

Overall the server process is exposing us a single process with two different methods to handle the setting and getting of item.
