string = input()


lower_arr = [ch for ch in string if ch.islower()]
upper_arr = [ch for ch in string if ch.isupper()]
even_arr = [ch for ch in string if ch.isdigit() and int(ch) % 2 == 0]
odd_arr = [ch for ch in string if ch.isdigit() and int(ch) % 2 != 0]

lower_arr.sort()
upper_arr.sort()
even_arr.sort()
odd_arr.sort()

new_arr = list(map(str, lower_arr+upper_arr+odd_arr+even_arr))
sort = ''.join(new_arr)
print(sort)


