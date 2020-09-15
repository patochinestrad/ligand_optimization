import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
import subprocess, shutil, os

cwd = os.getcwd()
pdbdir = cwd + '/test/'

test = pd.read_csv('test.csv', sep=',')
try:
    os.mkdir(pdbdir)
except:
    print('No se hizo el directorio, capaz ya existe?')



number = 0
for i in test['Smile']:
    print(i)
    number += 1
    m = Chem.MolFromSmiles(i)
    AllChem.EmbedMolecule(m)
    AllChem.UFFOptimizeMolecule(m)
    m.SetProp('_Name', str(i))
    f = open('mol_'+str(number)+'.pdb', 'a')
    f.write(Chem.MolToPDBBlock(m))
    f.close()


for x in os.listdir(cwd):
    if x.endswith('.pdb'):
        shutil.move(x, pdbdir)

nosepudo = []
os.chdir(pdbdir)
for y in os.listdir(pdbdir):
    try:
        subprocess.call(['C:/Program Files (x86)/MGLTools-1.5.6/python.exe', 'C:/Users/Pato/Desktop/LFM/Utilities24/prepare_ligand4.py', '-l', y, '-A hydrogens', '-U nphs_lps'])
    except:
        nosepudo.append(y)
print('No se pudo convertir a pdbqt los siguientes ligandos:', nosepudo)

pdbs = pdbdir + '/pdbs/'
pdbqts = pdbdir + '/pdbqts/'

try:
    os.mkdir('pdbs/')
    os.mkdir('pdbqts/')
except:
    print('no se pudo hacer alguno de los directorios de resultados, capaz ya existen?')

nosemovio = []
for x in os.listdir(pdbdir):
    if x.endswith('.pdb'):
        shutil.move(x, pdbs)
    elif x.endswith('.pdbqt'):
        shutil.move(x, pdbqts)
    else:
        nosemovio.append(x)
print('No se pudo mover los siguientes archivos a su carpeta correspondiente:', nosemovio)
