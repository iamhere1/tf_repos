#coding=utf8
"""
preprocess data in libsvm format
- for continous features, padding the missed feature with value zero
- for features with index begin from none zero(most situations with one), reset feature index begin with 0
"""

import sys
"""
process data function
- input_name: input feature file name
- output_name: output feature file name
- feature_num: feature number of the feature set
- begin_index: begin index feature of the feature set
"""
def format_data(input_name, output_name, feature_num, begin_index):
    infile = open(input_name, 'r')
    outfile = open(output_name, 'w')
    for line in infile:
        line = line.strip()
        str_vec = line.split(' ')
        if (len(str_vec) - 1) == feature_num:
            outfile.write(line)
        else:
            feature_dict = {}
            for i in range(1, len(str_vec)):
                temp_vec = str_vec[i].split(':')
                feature_index = int(temp_vec[0]) - begin_index
                if feature_index < 0:
                    continue
                feature_value = temp_vec[1]
                feature_dict[feature_index] = feature_value
            for i in range(feature_num):
                if False == feature_dict.has_key(i):
                    feature_dict[i] = "0" 
            res_line = str_vec[0]
            for (key, value) in sorted(feature_dict.items(), key = lambda pair:pair[0]):
                res_line = res_line + " " + str(key) + ":" + value
            outfile.write(res_line + "\n")
    infile.close()
    outfile.close()

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print ('Usage:<input_file> <output_file> <feature_num> <begin_index>')
        exit(0)
    input_name = sys.argv[1]
    output_name = sys.argv[2]
    feature_num = sys.argv[3]
    begin_index = sys.argv[4]
    format_data(input_name, output_name, int(feature_num), int(begin_index))

