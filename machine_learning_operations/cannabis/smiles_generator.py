# Imports
# -------

from rdkit import Chem
from global_chem import GlobalChem

if __name__ == '__main__':

    input_file = pd.read_csv('./chemical_list.csv', header=None, usecols=[0], names=["smiles"])
    smiles_list = input_file["smiles"].values.tolist()
    output_file = open('mol.smi', 'w') 
    
    for molecule in smiles_list:
        
        try:

            rdkit_molecule = Chem.MolFromSmiles(molecule)
            for i in range(1000):
                smiles = Chem.MolToSmiles(rdkit_molecule, doRandom=True)
                output_file.write(smiles + '\n')

        except:
            continue



