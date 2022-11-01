from secret import *


id = 61843152  #inserir id da conta


tweets = list()


for tweet in client(12).get_users_tweets(id=id, exclude='replies', max_results=100)[0]:
    tweets.append(tweet['id'])
    print(tweet['text'])


tweets


users = list()
aux = list()


import time
i = 1
while len(users) <= 200:
    print(tweets[i])
    if len(users) == 0:
        for user in client(12).get_liking_users(id=tweets[i])[0]:
            users.append(user['id'])
            
        i += 1
    else:
        try:
            for user in client(12).get_liking_users(id=tweets[i])[0]:
                if user['id'] not in users:
                    users.append(user['id'])
            i += 1
        except TypeError:
            i += 1
    time.sleep(1)


len(users)


from random import sample


n = 200


users = sample(users, n)


archive = open('Usuarios_camaradeputados.txt', 'a')


for i in users:
    aux.append(str(i) + '\n')



archive.writelines(aux)
archive.close()


