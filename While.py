import time
while True:
    print('a')
    break


num = 5
while True:
    print('b')
    num = num+1

    if num > 10:
        break


num = 5
while True:
    num = num+1

    if num == 10:
        continue
    print(num)
    time.sleep(2)