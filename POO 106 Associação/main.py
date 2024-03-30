from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# primeiro momento mostrando a independencia dos mesmos
print(escritor.nome)
print(caneta.marca)
maquina.escrever()

# segundo momento mostrando a assosciação ref CANETA
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

# Ainda no segundo momento mostrando a assosciação ref MAQUINA
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

# Explicando após a "morte" do escritor
del escritor
# Colocado o print(escritor) em comentario para ver o comportamento do código
# print(escritor)
print(caneta.marca)
maquina.escrever()
