from multiprocessing.managers import BaseManager


HOST = 'localhost'
PORT = 3456
PASSWORD = b'password'

manager = BaseManager((HOST, PORT), PASSWORD)

manager.register('get_item')
manager.register('add_item')
manager.connect()

item = manager.get_item("user")

print(item)
