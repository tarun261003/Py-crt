from abc import ABC,abstractmethod
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def query(self):
        pass
    @abstractmethod
    def update(self):
        pass
class MySQLConnector(DatabaseConnector):
    def __init__(self):
        self.username='tarun261003'
        self.password=2610
        self.is_connect=None
    def connect(self,user,passw):
        if user==self.username and passw==self.password:
            print('Connected...')
            self.is_connect=True
        else:
            print('Not connected ... Check details.')
            self.is_connect=False
    def query(self,qr):
        if self.is_connect:
            print(f'Executing {qr}')
            print('done')
        else:
            print('Failed....')
    def update(self,qr):
        if self.is_connect:
            print(f'Executing {qr}')
            print('Done updated.')
        else:
            print('Failed...')
m=MySQLConnector()
user=input('Enter the username:')
passw=int(input('Enter the password:'))
m.connect(user,passw)
m.query('"Select * from ABC"')
m.update('"Update column okok NO"')