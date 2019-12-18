passwordrange = [193651, 649729]

def find_passwords(passwordrange):
    password_list = []
    for password in range(passwordrange[0], passwordrange[1]+1):

        password = str(password)

        highestdigit = 0
        broke = False
        doubles = False
        lastdigit = 0
        repeateddigits = 0
        for digit in password:
            digit = int(digit)

            if digit < highestdigit:
                broke = True
                break
            elif digit == lastdigit:
                repeateddigits = repeateddigits + 1

            if digit > highestdigit:
                highestdigit = digit
                if repeateddigits == 1:
                    doubles = True
                repeateddigits = 0
            
            lastdigit = digit
        
        if repeateddigits == 1:
            doubles = True
        if doubles == True and not broke:
            password_list.append(password)

    return password_list

password_list = find_passwords(passwordrange)
print(password_list)
print(len(password_list))