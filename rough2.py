def number_palondrome(x, y=0, z=0):
    steps = 1
    y = str(x)
    y = y[::-1]
    z = x + int(y)
    end_sum = True
    while end_sum:
        if z == int(str(z)[::-1]):
            end_sum = False
            return(steps, z)
        else:
            x, y, z = z, str(x)[::-1], x + int(y)
            number_palondrome(x, y, z)
            steps += 1

x = number_palondrome(195)
print(x)