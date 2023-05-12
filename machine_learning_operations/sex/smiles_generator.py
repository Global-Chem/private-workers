# Imports
# -------

from rdkit import Chem
from global_chem import GlobalChem


if __name__ == '__main__':

    output_file = open('mol.smi', 'w')
    gc = GlobalChem()
    gc.build_global_chem_network()
    node_1 = list(gc.get_node_smiles('exsens_products').values())
    node_2 = list(gc.get_node_smiles('lube').values())    
    smiles_list = node_2 
#     smiles_list = smiles_list + jwh_compounds    
    
    for molecule in smiles_list:
        
        try:

            rdkit_molecule = Chem.MolFromSmiles(molecule)
            for i in range(10000):
                smiles = Chem.MolToSmiles(rdkit_molecule, doRandom=True)
                output_file.write(smiles + '\n')

        except:
            continue



