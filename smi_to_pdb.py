import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem

test = pd.read_csv('test.csv', sep=',')
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
