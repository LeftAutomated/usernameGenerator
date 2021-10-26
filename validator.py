import requests
from threading import Thread

noobs = []
threadc = 10

names = open('usernames.txt', 'r').read().splitlines()

def divide(stuff):
    return [stuff[i::threadc] for i in range(threadc)]

def validate(users):
    global noobs
    for user in users:
        try:
            if(requests.get(f'https://auth.roblox.com/v1/usernames/validate?request.username={user}&request.birthday=1337-04-20').json()['code']) == 0:
                noobs.append(user)
                print(user)
        except Exception as e:
            pass

print('Begin')

threads = []
for i in range(threadc):
    threads.append(Thread(target=validate, args=[divide(names)[i]]))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print('Write')

with open('valid.txt', 'a') as f:
    for noob in noobs:
        f.write(noob + '\n')

print('Done')
