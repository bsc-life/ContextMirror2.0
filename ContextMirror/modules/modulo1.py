from ContextMirror.modules.scripts.setup_data_sequential import *

from ContextMirror.modules.scripts.MT import *
import configparser
from halo import Halo

from ContextMirror.modules.scripts.PP import *

#read arguments
config = configparser.ConfigParser()
config.read('config.ini')
input_file=config.get('SETUP','input_file')
taxid=config.get('SETUP','taxid')
blastdir=config.get('SETUP','blastdir')
edirectdir=config.get('SETUP','edirectdir')
dbdir=config.get('MIRRORTREE','db')
commonsp_threshold=config.get('MIRRORTREE','common_species_treshold')

my_runs='./my_runs.txt'
my_runs_pairs='./my_runs_pairs.txt'
#call the setup script that prepares the data

def mirror_tree():
    spinner = Halo(text='Setting up data', spinner='dots')
    spinner.start()
    setup_data_sequential(input_file,taxid,blastdir,edirectdir,dbdir)
    spinner.stop()
    print("\nData ready to start analysis")
    spinner = Halo(text='MirrorTree', spinner='dots')
    spinner.start()
    tree_tree_matrix(my_runs, commonsp_threshold,my_runs_pairs)
    spinner.stop()
    spinner = Halo(text='Adding taxonomy information', spinner='dots')
    spinner.start()
    add_taxid()
    spinner.stop()
    print('Taxonomy information added')
    spinner = Halo(text='Aligning', spinner='dots')
    spinner.start()
    align()
    spinner.stop()
    print('Homologs aligned')
    spinner = Halo(text='Building tree', spinner='dots')
    spinner.start()
    tree()
    spinner.stop()
    print('Phylogenetic trees constructed')
    spinner = Halo(text='Building DM', spinner='dots')
    spinner.start()
    dm()
    spinner.stop()
    print('Distance matrices computed')
    spinner = Halo(text='Computing correlation', spinner='dots')
    spinner.start()
    corr()
    fill_tt()
    spinner.stop()
    print('Correlations calculated ... filling tree-tree matrix')
    print('\n\nTree-Tree correlation matrix completed successfully.')
