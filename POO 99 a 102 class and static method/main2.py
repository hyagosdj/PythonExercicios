# method vs @classmethod vs @staticmethod
# method - self, método de instância.
# @classmethod - clas, método de classe.
# @staticmethod - método estático (Sem Self, Sem Cls).

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): # método normal, recebe self.
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod # metodo de classe, recebe cls
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod # Ele é uma função dentro da classe | ele não recebe nem self, nem cls | Ele serve por conta de organização, quando precisa deixar ele dentro da classe.
    def log(msg):
        print('LOG', msg)

# c1 = Connection()
c1 = Connection.create_with_auth('luiz', '1234')
# c1.set_user('luiz')
# c1.set_password('123')
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)