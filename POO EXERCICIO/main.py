from ct_corre import ContaCorrente
from ct_poupa import ContaPoupanca

ct_corre = ContaCorrente(agencia=1010, conta=0000, saldo=0, limite=1000)
ct_corre.depositar(800)
ct_corre.sacar('1234')
