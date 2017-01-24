import os
import time
import timeit
import random
from A_star_misplaced_tiles import A_star_mt
from A_star_Manhattan import A_star_Mttn

#generate 20 random puzzles
N = list()
for i in range(1,21):
        n = random.randint(3,4)
        N.append(n)
        os.system("python3 puzzleGenerator.py" + " "+ str(n) + " " + str(random.randint(10,50)) + " " +"input_files/"+str(i)+".txt")

f = open('Heuristic_comparison_output.txt','w')

for i in range(1,21):
        #call A* misplaced tiles and manhattan distance on each
        #print len(Explored),time and final.g
        start_time_mt = timeit.default_timer()
        s1,explored_mt = A_star_mt(N[i-1],"input_files/"+str(i)+".txt")
        elapsed_mt = timeit.default_timer() - start_time_mt

        start_time_mttn = timeit.default_timer()
        s2,explored_mttn = A_star_Mttn(N[i-1],"input_files/"+str(i)+".txt")
        elapsed_mttn = timeit.default_timer() - start_time_mttn

        f.write(str(i)+".txt: N="+str(N[i-1]))
        f.write("\n")
        f.write("Misplaced tiles: number of states explored:" +str(explored_mt)+" time taken:"+str(elapsed_mt * 1000) + " Depth:" + str(s1.g) +"\n")
        f.write("Manhattan dist: number of states explored:" +str(explored_mttn)+" time taken:"+str(elapsed_mttn * 1000) + " Depth:" + str(s2.g) +"\n")

f.close()