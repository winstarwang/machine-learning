import os

for i in range(1,4):
    for j in range(1,6):
        cmd = "python run_search -p{0} -s{1} > p_{0}_s{1}.txt".format(i,j)
        print(cmd)
        # os.system(cmd)