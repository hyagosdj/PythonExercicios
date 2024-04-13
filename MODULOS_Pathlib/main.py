from pathlib import Path

#from shutil import rmtree

# caminho_projeto = Path()
# print(caminho_projeto.absolute())

# caminho_arquivo = Path(__file__)

# print(caminho_arquivo)
# print(caminho_arquivo.parent)
# print(caminho_arquivo.parent.parent.parent)

# ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')

# arquivo = Path.home() / 'Desktop' / 'arquivo.txt'



caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo.touch() # Atualiza criando um novo arquivo/diretorio
caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.json'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey')

# caminho_pasta.rmdir() # não da pra apagar a pasta todo de uma vez.. tem que ser feito do ultimo doc/pasta e vindo até a principal

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

# Criando varios arquivos
for i in range(10):
    file = files / f'file_{i}.txt'
    file.touch()

    if file.exists(): # .is_file() é ou nao arquivo // .is_dir() é ou nao diretorio
        file.unlink()
    else:
        file.touch()
    # Abrir e escrever o que deseja
    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file{i}.txt')

# Entrar na pasta e vir excluindo de dentro pra fora
# rmtree(caminho_pasta)

def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'): # **/*.txt (vem todos os arquivos txt)
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, remove_root=False)
            file.rmdir()
        else:
            file.unlink()
    if remove_root:
        root.rmdir()

rmtree(caminho_pasta)

# caminho_arquivo.write_text('')
# with caminho_arquivo.open('+a') as file:
    # file.write('Uma linha\n')
    # file.write('Outra linha\n')

# print(caminho_arquivo.read_text())
# arquivo.touch() # Cria um arquivo no caminho indicado.
# arquivo.unlink() # Deleta o arquivo no caminho indicado.
# arquivo.write_text('Olá mundo.')
# arquivo.write_text('Olá de novo.')
# print(arquivo.read_text()) # Ler o conteúdo do arquivo do caminho indicado.

# print(Path.home() / 'Desktop' / 'arquivo.txt')
