questions =['name', 'quest', 'favorite color']
answers =['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


for i in reversed(range(1, 10, 2)):
    print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

for f in sorted(set(basket)):
    print(f)
    