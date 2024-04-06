# from dataclasses import dataclass


# @dataclass(repr=True)
# class Pessoa:
#     nome: str
#     sobrenome: str


# if __name__ == '__main__':
#     lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
#     ordenadas = sorted(lista, reverse=True, key=lambda p: p.nome)
#     print(ordenadas)

# from dataclasses import asdict, astuple, dataclass


# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str


# if __name__ == '__main__':
#     p1 = Pessoa('Luiz', 'Otávio')
#     print(asdict(p1).keys())
#     print(asdict(p1).values())
#     print(asdict(p1).items())
#     print(astuple(p1)[0])

from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    nome: str = field(
        default='Missing', 
    )
    sobrenome: str = 'Not send'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(fields(p1))
    print(p1)