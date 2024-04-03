from cc import ContaCorrente
from cp import ContaPoupanca

# Não se pode instanciar uma conta, tem que instanciar a especialização da conta.
# from conta import Conta

cp = ContaPoupanca(1111, 2222, 0)
cp.sacar(10)
cp.depositar(10)
cp.sacar(10)
cp.sacar(10)

# Exemplo da não instanciação.
# conta = Conta(1111, 2222, 0)

print('\n'+'#' * 30 +'\n')

cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
# cc.sacar()