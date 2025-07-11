#create a seample collection
users={'Hans':'active','Eleonore':'inactive','Ban':'active'}
for user,status in users.copy().items(): #strategy: Iterate over acopy
    if status =='inactive':
        del users[user]
active_users={} #strategy: Iterate over a copy
for user,status in users.copy().items():
    if status =='active':
        active_users[user]=status
