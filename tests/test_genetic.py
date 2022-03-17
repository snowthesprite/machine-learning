import sys
sys.path.append('src')
from genetic_tic_toe import *

#s = '123456789'
#print(s[:2] + '0' + s[3:])
print(random.choice([1,2]))

gene = GeneticAlgorithm(25)
mate = gene.mate(gene.find_top_5(gene.original_gen))
print(len(mate))