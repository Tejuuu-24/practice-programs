num = int(input())#13 1101
i = int(input())#2
if num & (1 << i):  #1101
    print("1")      #0100
else:
    print("0")