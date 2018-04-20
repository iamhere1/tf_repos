#coding=utf8
"""
split data into two subset
- each row is randomly selected into the first file or the second file
- the probility of each row falled into the two files are k/nold and 1-k/nold
"""

import sys
import random
"""
split function
- input_name: input file name
- sample_name1: each row falled into this file is k/nold
- sample_name2: each row falled into this file is 1-k/nold
- k: random integer falling between [1, k] indicate the row falling into the first file
- nfold: the max number of the random integer value
"""
def sample_data(input_name, sample_name1, sample_name2, k, nfold):
    input_file = open(input_name, 'r')
    sample_file1 = open(sample_name1, 'w')
    sample_file2 = open(sample_name2, 'w')
     
    random.seed()
    for line in input_file:
        line = line.strip()
        sample_index = random.randint(1, nfold)
        if sample_index <= k:
            sample_file1.write(line + "\n")
        else:
            sample_file2.write(line + "\n")
    input_file.close()
    sample_file1.close()
    sample_file2.close()

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print ('Usage:<input_file> <sample_file1> <sample_file2> <k> <nfold>')
        exit(0)
    input_name = sys.argv[1]
    sample_name1 = sys.argv[2]
    sample_name2 = sys.argv[3]
    k = int(sys.argv[4])
    nfold = int(sys.argv[5])
    sample_data(input_name, sample_name1, sample_name2, k, nfold)

