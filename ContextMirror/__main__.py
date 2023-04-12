import argparse
from modules.modulo1 import *
from modules.modulo2 import *
from modules.modulo3 import *



def main():
	args = inputparameters()
	who = args.module
	if who == 'MirrorTree':
		modulo1()
	elif who == 'PPcorrelation':
	    modulo2()
	elif who == 'PartialCorrelation':
	    modulo3()
	elif who == 'CM':
		modulo1()
		modulo2()
		modulo3()


def inputparameters():
	parser = argparse.ArgumentParser(description='This library performs the different steps of the CotnextMirror approach')
	parser.add_argument("-m", "--module", choices=['MirrorTree', 'PPcorrelation','PartialCorrelation', 'CM'], help = "Select your modules")
	
	args = parser.parse_args()
	return args

    
if __name__ == "__main__":
	main() 



