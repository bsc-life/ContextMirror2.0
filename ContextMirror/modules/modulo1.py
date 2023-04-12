from ContextMirror.modules.scripts.setup_data_parallel import *
from ContextMirror.modules.scripts.setup_data_sequential import *

from ContextMirror.modules.scripts.MT import *
import configparser
from halo import Halo

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
    # Prompt user to choose a mode
    mode = input("Choose mode: Parallel or Sequential? ")

    # Import and call the appropriate function based on the user's choice
    if mode == "Parallel":
        setup_data_parallel(input_file,taxid,blastdir,edirectdir,dbdir)
    elif mode == "Sequential":
        spinner = Halo(text='Setting up data', spinner='dots')
        spinner.start()
        setup_data_sequential(input_file,taxid,blastdir,edirectdir,dbdir)
        spinner.stop()
        print("\nData ready to start analysis")
        spinner = Halo(text='MirrorTree', spinner='dots')
        spinner.start()
        tree_tree_matrix(my_runs, commonsp_threshold,my_runs_pairs)
        spinner.stop()
        print("\n\nTree-Tree correlation matrix completed successfully.")

    else:
        print("Invalid mode. Choose either Parallel or Sequential.")
