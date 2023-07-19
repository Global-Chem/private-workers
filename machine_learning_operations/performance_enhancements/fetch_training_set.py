# Imports
# -------

import os
import json
import requests
from rdkit import Chem
from rdkit.Chem import Draw

if __name__ == '__main__':

    input_file = pd.read_csv('./chemical_list.csv', header=None, usecols=[0], names=["smiles"])
    smiles_list = input_file["smiles"].values.tolist()
    
    for smiles in smiles_list:

        try:
            molecule = Chem.MolFromSmiles(smiles)
            print (molecule)
            molecules.append(molecule)
        except:
            continue
      
    images = Draw.MolsToGridImage(
      molecules,
      molsPerRow=10,
      subImgSize=(200,200),
    )

    images.save('training_set.png')
