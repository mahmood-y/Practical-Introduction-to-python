'''15. Use a list comprehension to create the list below, which consists of ones separated by increasingly
many zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]'''

lst = [int(str_num[y])
       for str_num in [f'{"1"}{"0"*i}{"1"*(i // 10)}' for i in range(11)]
         for y in range(len(str_num))]

print(lst)
