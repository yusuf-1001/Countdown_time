import time

select_time=int(input("Enter the time in seconds: "))

for i in range(select_time,0,-1):
    seconds=i % 60
    mınutes=int(i/60)%60
    hours=int(i / 3600)
    print(f'{hours:02}:{mınutes:02}:{seconds:02}')
    time.sleep(1)
print("TİME'S UP!")