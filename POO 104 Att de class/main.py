
class A:
    vc = 123

    def __init__(self):
        pass

a1 = A()
a2 = A()

A.vc = 'ALTERADO'

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print()

print(a1.vc)
print(a2.vc)
print(A.vc)
