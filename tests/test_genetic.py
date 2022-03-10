import sys
sys.path.append('src')
from genetic_tic_toe import *

gene = GeneticAlgorithm(25)
print(gene.find_top_5())