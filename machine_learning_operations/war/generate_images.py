# Imports
# -------

import os
import json
import requests
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

    token = os.getenv('GITHUB_TOKEN')

    headers = {
        "Accept": 'Accept: application/vnd.github+json',
        "Authorization" : "token {}".format(token)
    }

    data = {
        "title": "War Run",
        "body": "%s" % smiles_list

    }

    username = 'Global-Chem'
    repository_name = 'Chemical-Ecosystem'

    url = "https://api.github.com/repos/{}/{}/issues".format(
           username,
           repository_name
    )

    response = requests.post(
         url,
         data=json.dumps(data),
         headers=headers

    )

    print (response.content)

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

    images.save('results.png')
