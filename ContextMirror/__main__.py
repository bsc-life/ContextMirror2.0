import argparse
from modules.modulo1 import *
from modules.modulo2 import *

def main():
	args = inputparameters()
	who = args.module
	if who == 'MirrorTree':
	    mirror_tree()
	elif who == 'ContextMirror':
	    mirror_tree()
		context_mirror()

def inputparameters():
	parser = argparse.ArgumentParser(description='This library performs MirrorTree and ContextMirror')
	parser.add_argument("-m", "--module", choices=['MirrorTree','ContextMirror'], help = "Select your module")
	
	args = parser.parse_args()
	return args

    
if __name__ == "__main__":
	main() 



