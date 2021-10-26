cha = 'abcdefghijklmnopqrstuvwxyz0123456789'

for a in cha:
    for b in cha:
        for c in cha:
            for d in cha:
                word = a + b + c + d
                with open('usernames.txt', 'a') as f:
                    f.write(word + '\n')
print('done')
