n = input()
new_arr = ''

for i in range(0, len(n)):
    if((n[i] < "A" or n[i] > "Z") and (n[i] < "А" or n[i] > "Я")):
        new_arr += n[i]

print(new_arr)
