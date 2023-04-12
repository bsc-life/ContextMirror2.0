from ContextMirror.modules.scripts.setup_data import *
from ContextMirror.modules.scripts.MT import *
from ContextMirror.modules.scripts.MT2 import *
import time

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

def context_mirror():
    # Prompt user to choose a mode
    mode = input("Choose mode: Cluster or Local? ")

    # Import and call the appropriate function based on the user's choice
    if mode == "Cluster":
        setup_data_parallel(input_file,taxid,blastdir,edirectdir,dbdir)
    elif mode == "Local":
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print('Start: '+str(current_time))
        #spinner = Halo(text='Setting up data\n', spinner='dots')
        #spinner.start()
        #setup_data(input_file,taxid,blastdir,edirectdir,dbdir)
        #spinner.succeed('Data ready to start analysis')
        #print('\n\n######################################################################################################################\n\n                                                 MirrorTree                                        \n\n')
        #spinner = Halo(text='\n\nMirrorTree\n', spinner='dots')
        #spinner.start()
        #tree_tree_matrix(my_runs, commonsp_threshold,my_runs_pairs)
        #spinner.succeed('\n\nTree-Tree correlation matrix completed successfully.\n')
        #add_taxid()
        #spinner = Halo(text='Alignment\n', spinner='dots')
        #spinner.start()
        #align()
        #spinner.succeed("\nMultiple sequence alignments completed successfully")
        #spinner = Halo(text='Phylogenetic trees\n', spinner='dots')
        #spinner.start()
        #tree()
        #spinner.succeed("\n\nPhyloegentic trees built successfully.")
        spinner = Halo(text='Extracting distance matrices\n', spinner='dots')
        spinner.start()
        dm()
        spinner.succeed("\n\nDistance matrices extracted successfully from phylogenetic trees.")
        spinner = Halo(text='Computing correlations\n', spinner='dots')
        spinner.start()
        corr()
        spinner.succeed("\n\nAll correlations computed.")
        tt = time.localtime()
        final_time = time.strftime("%H:%M:%S", t)
        print(final_time)

    else:
        print("Invalid mode. Choose either Cluster or Local.")

