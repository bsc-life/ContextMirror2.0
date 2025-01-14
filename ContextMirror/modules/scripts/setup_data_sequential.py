import subprocess
import os


currentdir=os.path.dirname('../')

def setup_data_sequential(input_file,taxid,blastdir,edirectdir,dbdir):
    #process = subprocess.run('./setup.sh %s %s %s %s' %(input_file,taxid,blastdir,edirectdir), shell=True, check=True) 
    subprocess.call('bash %s/ContextMirror/modules/scripts/setupscripts/setup_sequential.sh %s %s %s %s %s' %(currentdir,input_file,taxid,blastdir,edirectdir,dbdir),shell=True)
    
    
