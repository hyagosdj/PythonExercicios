from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            # Primeiro Momento:
            # print(f'{self._nome} não está ligado para conectar.')
            
            # Segundo momento com interação do LogMixin
            info = f'{self._nome} não está ligado para conectar.'
            print(info)
            self.log_info(info)
            return
        
        if self._conectado:
            # Primeiro Momento:
            #print(f'{self._nome} já está conectado.')

            # Segundo momento com interação do LogMixin
            error = f'{self._nome} já está conectado.'
            print(error)
            self.log_error(error)
            return
        # Primeiro Momento:
        # print(f'{self._nome} está conectado.')
        
        # Segundo momento com interação do LogMixin
        info = f'{self._nome} está conectado.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self): 
        """ if not self._ligado:
            print(f'{self._nome} está desligado.')
            return """

        if not self._conectado:
            # Primeiro Momento:
            # print(f'{self._nome} já está desconectado.')

            # Segundo momento com interação do LogMixin
            error = f'{self._nome} já está desconectado.'
            print(error)
            self.log_error(error)
            return

        # Primeiro Momento:
        # print(f'{self._nome} está desconectado.')

        # Segundo momento com interação do LogMixin
        info = f'{self._nome} está desconectado.'
        print(info)
        self.log_info(info)
        self._conectado = False