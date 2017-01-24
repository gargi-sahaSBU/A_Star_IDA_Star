from A_star_search import A_STAR 
from IDA_star import IDA_STAR 
import sys


'''
python puzzleSolver.py <#Algorithm> <N> <INPUT_FILE_PATH> <OUTPUT_FILE_PATH>

'''
Algorithm = int(sys.argv[1])
N = int(sys.argv[2])
input_file = sys.argv[3]
output_file = open(sys.argv[4],'w')

if Algorithm == 1:
	output_file.write(A_STAR(input_file,N))
elif Algorithm == 2:
	output_file.write(IDA_STAR(input_file,N))

output_file.close()



