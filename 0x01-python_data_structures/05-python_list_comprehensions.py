vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruit = [' banana', ' loganberry', 'possion fruit ']
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])
# the tuple must be parenthesized , otherwise an error is raised 
print([x, x**2 for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
