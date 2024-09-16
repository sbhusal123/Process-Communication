from multiprocessing.managers import BaseManager


HOST = '0.0.0.0'
PORT = 3456
PASSWORD = b'password'

manager = BaseManager((HOST, PORT), PASSWORD)

manager.register('add_item')
manager.connect()

manager.add_item("user", {
    "name": "surya bhusal", 
    "email": "test@gmail.com"
})

