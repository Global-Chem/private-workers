# Imports
# -------

from rdkit import Chem
from global_chem import GlobalChem


jwh_compounds = [
 'c14ccccc4cccc1C(=O)c3c2ccccc2n(c3C)CCCCC',
 'CCCN1C(=C(C2=CC=CC=C21)C(=O)C3=CC=CC4=CC=CC=C43)C',
 'CCCCCN1C=C(C(C2=CC=CC3=CC=CC=C32)=O)C4=CC=CC=C41',
 'c3cccc2c3cccc2C(=O)c1cn(CCCCCC)c4c1cccc4', 
 'CCCCCn3cc(cc3)C(=O)c1cccc2ccccc12',
 'CCCCn1c(c(c2c1cccc2)C(=O)c3cccc4c3cc(cc4)C)C',
 'CCCCCN1C(=C(C2=CC=CC=C21)C(=O)C3=CC=CC4=C3C=C(C=C4)C)C',
 'CCCCCCC(C)(C)C1=CC2=C(C=C1)[C@@H]3CC(=CC[C@H]3C(O2)(C)C)CO',
 'CCCCCCC(C)(C)C1=CC2=C(C=C1)[C@@H]3CC(=CC[C@H]3C(O2)(C)C)C',
 'CCCCN1C=C(C2=CC=CC=C21)C(=O)C3=CC=CC4=CC=CC=C43',
 'CCCCN1C=C(C2=CC=CC=C21)C(=O)C3=CC=CC4=CC=CC=C43',
 'CCCCCCCc3cc2OC(C)(C)[C@@H]1CCC(C)=C[C@H]1c2c(O)c3',
 'CCCCCn(c1C)c2ccccc2c1C(=O)c(ccc3OC)c4ccccc34',
 'CCCCCN1C2=CC=CC=C2C(=C1CC)C(=O)C3=CC=CC4=CC=CC=C43',
 'CCCN1C=C(C2=CC=CC=C21)C(=O)C3=CC=C(C4=CC=CC=C43)C',
 'CCCCCn1cc(c2c1cccc2)C(=O)c3ccc(c4c3cccc4)C',
 'CCCCC1=CC2=C([C@@H]3C=C(CC[C@H]3C(O2)(C)C)C)C(=C1)O',
 'O3c1cc(ccc1[C@@H]2C\C(=C/C[C@H]2C3(C)C)C)C(C)(C)CCC',
 'OC1=C2[C@]3([C@](C(C)(C)OC2=CC(CCCCCCCC)=C1)(CCC(C)=C3)[H])[H]',
 'O=C(C1=CN(CCCCC)C(C2=CC=CC=C2)=C1)C3=C(C=CC=C4)C4=CC=C3',
 'O=C(C1=CC=CC2=C1C=CC=C2)C3=CN(CCCCCCC)C(C4=CC=CC=C4)=C3',
 'c4ccccc4-c2cc(cn2CCCCCC)C(=O)c1cccc3c1cccc3',
 'CCCN1C(=C(C2=CC=CC=C21)C(=O)C3=CC=C(C4=CC=CC=C43)C)C',
 'c4cccc1c4c(ccc1C)C(=O)c3c2ccccc2n(c3C)CCCCC',
 'CCCCN1C=C(C=C1C2=CC=CC=C2)C(=O)C3=CC=CC4=CC=CC=C43',
 'Oc3c5c1ccccc1n(c5cc2OC([C@@H]4CC/C(=C\[C@H]4c23)C)(C)C)CCCCC',
 'CCCCCn(c4)c1ccccc1c4C(=O)c2cccc(cc3)c2cc3OC',
 'CCCCCn1cc(c2c1cccc2)C(=O)Cc3ccccc3',
 'c3cccc2c3cccc2Cc(cn4CCCCC)c1ccccc14',
 'CCCCCC1=C\C(=C/c2cccc3ccccc32)c2ccccc21',
 'c4cccc2c4c(CC)ccc2C(=O)c(c3)c1ccccc1n3CCCCC',
 'CCCCCn1cc(c2c1cccc2)Cc3ccc(c4c3cccc4)C',
 'CCCCCn1cc(c2c1cccc2)Cc3ccc(c4c3cccc4)OC',
 'c3cccc1c3c(ccc1C)C(=O)c5c2ccccc2n(c5)CCN4CCOCC4',
 'CCCCCn1c(c(c2c1cccc2)Cc3cccc4c3cccc4)C',
 'C4COCCN4CCn2cc(c5ccccc25)C(=O)c3c1ccccc1c(OC)cc3',
 'O=C(C1=CC=CC2=C1C=CC=C2)C3=CN(C4=C3C=CC=C4)CCN5CCOCC5',
 'Clc2ccccc2CC(=O)c1cn(CCCCC)c3ccccc13',
 'c4cccc2c4c(CC)ccc2C(=O)c(c3)c1ccccc1n3CCCCC',
 'CCCCCn1cc(c2c1cccc2)C(=O)Cc3ccccc3Br',
 'COc2ccccc2CC(=O)c(c3ccccc13)cn1CCCCC',
 'O=C(c2c1ccccc1n(c2)CCCCC)Cc3ccccc3C',
 'c2ccc(OC)cc2CC(=O)c(cn1CCCCC)c3ccccc13',
 'CCCCCN1C=C(C=C1C2=CC=CC=C2F)C(=O)C3=CC=CC4=CC=CC=C43',
 'CCCCCN1C=C(C=C1C2=CC=CC3=CC=CC=C32)C(=O)C4=CC=CC5=CC=CC=C54',
 'C[C@H](CC)C(C)(C)c1cc2OC(C)(C)[C@@H]3CC=C(C)C[C@H]3c2c(OC)c1',
]

if __name__ == '__main__':

    output_file = open('mol.smi', 'w')
    gc = GlobalChem()
    gc.build_global_chem_network()
    smiles_list = list(gc.get_node_smiles('phytocannabinoids').values())
    smiles_list = smiles_list + jwh_compounds    
    
    for molecule in smiles_list:
        
        try:

            rdkit_molecule = Chem.MolFromSmiles(molecule)
            for i in range(1000):
                smiles = Chem.MolToSmiles(rdkit_molecule, doRandom=True)
                output_file.write(smiles + '\n')

        except:
            continue



