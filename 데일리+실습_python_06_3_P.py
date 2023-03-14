# count_vowels('apple') #=> 2
# count_vowels('banana') #=> 3

def count_vowels(str):
    count = 0
    vowels = ['a','e','i','o','u']
    for i in str:
        if i in vowels:
            count = count + 1
        
    print(count)

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3


        
