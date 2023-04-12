import subprocess
import os


currentdir=os.path.dirname('../')

def setup_data(input_file,taxid,blastdir,edirectdir,dbdir):
    subprocess.call('bash %s/ContextMirror/modules/scripts/setupscripts/setup.sh %s %s %s %s %s' %(currentdir,input_file,taxid,blastdir,edirectdir,dbdir),shell=True)
    
    
