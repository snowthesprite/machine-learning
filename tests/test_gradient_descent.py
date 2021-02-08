import sys
sys.path.append('src')
from gradient_descent import GradientDescent

def single_variable_function(x):
    return (x-1)**2
def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3
def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4
def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6

print('Does GradientDescent work for a single variable function?')
minimizer = GradientDescent(f=single_variable_function, initial_point=[0])
assert minimizer.point == [0], 'The inital point was off'
ans = minimizer.compute_gradient(delta = 0.01)
ans_rounded = [round(num, 3) for num in ans]
assert ans_rounded == [-2.000], 'The rounded gradient wasnt quite right' #rounded to 5 decimal places
minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
point_rounded = [round(num, 3) for num in minimizer.point]
assert point_rounded == [0.002], 'The rounded final answer wasnt quite right'
print('Yes, it does!', "\n")

print('Does GradientDescent work for a two variable function?')
minimizer = GradientDescent(f=two_variable_function, initial_point=[0,0])
assert minimizer.point == [0,0], 'The inital point was off'
ans = minimizer.compute_gradient(delta = 0.01)
ans_rounded = [round(num, 3) for num in ans]
assert ans_rounded == [-2.000, 3.000], 'The rounded gradient wasnt quite right'
minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
point_rounded = [round(num, 3) for num in minimizer.point]
assert point_rounded == [0.002, -0.003], 'The rounded final answer wasnt quite right'
print('Yes, it does!', "\n")

print('Does GradientDescent work for a three variable function?')
minimizer = GradientDescent(f=three_variable_function, initial_point=[0,0,0])
assert minimizer.point == [0,0,0], 'The inital point was off'
ans = minimizer.compute_gradient(delta = 0.01)
ans_rounded = [round(num, 3) for num in ans]
assert ans_rounded == [-2.000, 3.000, -4.000], 'The rounded gradient wasnt quite right'
minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
point_rounded = [round(num, 3) for num in minimizer.point]
assert point_rounded == [0.002, -0.003, 0.004], 'The rounded final answer wasnt quite right'
print('Yes, it does!', "\n")

print('Does GradientDescent work for a six variable function?')
minimizer = GradientDescent(f=six_variable_function, initial_point=[0,0,0,0,0,0])
assert minimizer.point == [0,0,0,0,0,0], 'The inital point was off'
ans = minimizer.compute_gradient(delta = 0.01)
ans_rounded = [round(num, 3) for num in ans]
assert ans_rounded == [-2.000, 3.000, -4.000, 1.000, 2.000, 3.000], 'The rounded gradient wasnt quite right'
minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
point_rounded = [round(num, 3) for num in minimizer.point]
assert point_rounded == [0.002, -0.003, 0.004, -0.001, -0.002, -0.003], 'The rounded final answer wasnt quite right'
print('Yes, it does!', "\n")
