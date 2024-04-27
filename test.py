s= '58 60 48 55 56 46 54 50 49 51 53 54 53'
s2 = '32 52 30 42 44 52 55 29 29 31 43 46 41 34 51 36 30'

l = [float(thing) for thing in s.split(' ')]

l2 = [float(thing) for thing in s2.split(' ')]
mean = sum(l)/len(l)
mean2 = sum(l2)/len(l2)
l.sort()
l2.sort()
print(l)
print()
print(l2)
print()
print('sum', sum(l), sum(l2))
print('len', len(l), sum(l2))
print('mean', mean, mean2)
print('summation', sum([(thing - mean)**2 for thing in l]), sum([(thing - mean)**2 for thing in l2]))