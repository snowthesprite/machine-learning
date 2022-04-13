import sys
sys.path.append('src')
from genetic_tic_toe import *

gene = GeneticAlgorithm(24)
print('ran')
gen_scores = gene.for_generation(100)

import matplotlib.pyplot as plt
plt.style.use('bmh')

generation = []
avg_vs_1 = []
avg_vs_prev = []
win_freq = []
block_freq = []


for (gen, scores) in gen_scores.items() :
    generation.append(gen)
    avg_vs_1.append(scores['vs_1'])
    avg_vs_prev.append(scores['vs_prev'])
    win_freq.append(scores['freq'][0])
    block_freq.append(scores['freq'][1])

plt.plot(generation, avg_vs_1)
plt.savefig('Vs_1.png')
plt.clf()
plt.plot(generation, avg_vs_prev)
plt.savefig('Vs_prev.png')
plt.clf()
plt.plot(generation, win_freq)
plt.savefig('win_freq.png')
plt.clf()
plt.plot(generation, block_freq)
plt.savefig('block_freq.png')


