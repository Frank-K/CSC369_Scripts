import sys
import random

def main():

	if len(sys.argv) < 2:
		print 'Usage: generateTrafficFile.py int'
		print '    int : Number of entries'
		return -1


	param_1 = sys.argv[1]

	if int(param_1) < 1:
		print 'Usage: generateTrafficFile.py int'
		print '    int : Number of entries'
		return -1


	generateFile(int(param_1))

	return 0


def generateFile(numCars):

	with open('trafficFile.txt', 'w') as f:

		for x in range (numCars):
			
			id = x
			in_dir = random.randint(0,3);
			out_dir = random.randint(0,3);

			f.write(str(id) + ' ' + str(in_dir) + ' ' + str(out_dir) + '\n')

	f.closed


main()