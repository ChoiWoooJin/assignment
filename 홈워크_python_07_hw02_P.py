def collatz(num):
    n = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            n = n + 1
        elif num % 2 == 1:
            num = (num*3)+1
            n = n + 1
            if n > 500:
                return -1
    return n
            
    

print(collatz(6)) #=> 8
print(collatz(16)) #=> 4
print(collatz(27)) #=> 111
print(collatz(626331)) #=> -1




