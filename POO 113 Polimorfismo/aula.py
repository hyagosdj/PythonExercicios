from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None: # o (-> None) é só para avisar para nós dev's o que deve ser retornado por aquela class expecifica.
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool: 
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self): 
        print('SMS: enviando - ', self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')

notificacao_email = NotificacaoEmail('Testando email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando sms')
notificar(notificacao_sms)
