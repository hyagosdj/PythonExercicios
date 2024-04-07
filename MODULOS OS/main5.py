import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'DESKTOP')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)

shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')