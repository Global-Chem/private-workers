# Imports
# -------

import os
from rdkit import Chem
from rdkit.Chem import Draw

if __name__ == '__main__':

    file = ''.join(open('./results.out', 'r').readlines())
    lines = file.split(' Best recorded SMILES: ')[1].split('\n')

    smiles_list = []
    molecules = []

    for line in lines:
        if 'Score' in line:
            continue
        elif '*' in line:
            continue
        elif line.strip() == '':
            continue
        else:
          smiles = line.split()[-1].strip()
          smiles_list.append(smiles)

    for smiles in smiles_list:

        try:
            molecule = Chem.MolFromSmiles(smiles)
            molecules.append(molecule)
        except:
            continue

    images = Draw.MolsToGridImage(
      molecules,
      molsPerRow=4,
      subImgSize=(200,200),
    )

    images.save('results.png')
