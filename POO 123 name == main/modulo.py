def soma(x: float, y: float) -> float:
    return x + y

def main() -> None:
    print(soma(10, 20))
    print(soma(20, 20))

# Serve para isolar a chamados de cada arquivo
if __name__ == '__main__':
    main()