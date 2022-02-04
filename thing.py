values = [5, 2]

x = lambda a : a
y = lambda b : values[1]*x(b)
z = lambda c : values[0] + values[1] * x(c) - y(c)
#z = lambda c, d : d(c)

#print(z(1, (lambda *prev : sum(prev))(x, y)))
print(z(1))

values = [7,8]

print(z(1))