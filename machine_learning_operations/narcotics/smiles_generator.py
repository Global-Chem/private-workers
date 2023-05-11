# Imports
# -------

from rdkit import Chem
from global_chem import GlobalChem


if __name__ == '__main__':

    output_file = open('mol.smi', 'w')
    gc = GlobalChem()
    gc.build_global_chem_network()
    node_1 = list(gc.get_node_smiles('schedule_one').values())
    node_2 = list(gc.get_node_smiles('schedule_two').values())
    node_3 = list(gc.get_node_smiles('schedule_three').values())
    node_4 = list(gc.get_node_smiles('schedule_four').values())
    node_5 = list(gc.get_node_smiles('schedule_five').values())
    node_6 = list(gc.get_node_smiles('pihkal').values())
    smiles_list = node_1 + node_2 + node_3 + node_4 + node_5 + node_6
#     smiles_list = smiles_list + jwh_compounds    
    
    for molecule in smiles_list:
        
        try:

            rdkit_molecule = Chem.MolFromSmiles(molecule)
            for i in range(1000):
                smiles = Chem.MolToSmiles(rdkit_molecule, doRandom=True)
                output_file.write(smiles + '\n')

        except:
            continue



