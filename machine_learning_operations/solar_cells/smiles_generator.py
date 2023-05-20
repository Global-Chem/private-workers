# Imports
# -------

from rdkit import Chem
from global_chem import GlobalChem

# Solar Cell Compounds

solar_cells = [
  'CC1=NC=NC=N1',
  'CC1=CC=C(C)C=C1',
  'CC1=CC=C(C)N=C1',
  'CC1=CC=C(C)[Se]1',
  'CC1=CC=C(C)C1',
  'CC1=NC=C(C)S1',
  'CC1=CC=C(C)S1',
  'CC1=CC=C(C)O1',
  'CC1=CC=C(C)N1',
  'CC1=CC=C(C)[SiH2]1',
  'CC1=C2C(C=C[Se]2)=C(C)S1',
  'CC1=C2C(C=CS2)=C(C)S1',
  'CC1=C2C(C=C[SiH2]2)=C(C)S1',
  'CC1=C2C(C=CN2)=C(C)S1',
  'CC1=C2C(C=CO2)=C(C)S1',
  'CC1=C2C(C=CC2)=C(C)S1',
  'CC1=C2C(N=CC=N2)=C(C)S1',
  'CC1=CC=C(C)C2=NSN=C21',
  'CC1=CC=C(C)C2=COC=C21',
  'CC1=CC=C(C)C2=CSC=C21',
  'CC1=CC=C(C)C2=C1C=CC=C2',
  'CC1=CC=C(C)C2=C[SiH2]C=C12',
  'CC1=CC=C(C)C2=CNC=C12',
  'CC1=CC=C(C)C2=CCC=C12',
  'CC1=CN=C(C)C2=NSN=C12',
  'CC1=C2C3=CC=CC=C3C4=CC=CC=C4C2=C(C)S1'
]

if __name__ == '__main__':

    output_file = open('mol.smi', 'w')
    gc = GlobalChem()
    gc.build_global_chem_network()
    smiles_list = solar_cells 
#     smiles_list = smiles_list + jwh_compounds    
    
    for molecule in smiles_list:
        
        try:

            rdkit_molecule = Chem.MolFromSmiles(molecule)
            for i in range(10000):
                smiles = Chem.MolToSmiles(rdkit_molecule, doRandom=True)
                output_file.write(smiles + '\n')

        except:
            continue



