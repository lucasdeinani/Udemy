# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user): # método de instância
        # setter
        self.user = user
    
    def set_password(self, password): # método de instância
        # setter
        self.password = password

    @classmethod # método de classe
    def create_with_auth(cls, user, password): # método de classe
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)

def connection_log(msg):
    print('LOG:', msg)

c1 = Connection.create_with_auth('luiz', '1234')
# c1 = Connection()
# print(c1.user)
# print(c1.password)
# c1.set_user('luiz')
# c1.set_password('123')
Connection.log('Essa é a mensagem de log')
print(c1.user)
print(c1.password)