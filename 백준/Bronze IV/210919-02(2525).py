
hour, minutes = map(int,input().split())
cook_time = int(input())
print((hour+((minutes+cook_time)//60))%24, (minutes+cook_time)%60)  




