
input = [5, 8, 2, 4, 4, 3, 7, 9]
for i in range(len(input)):
    if i == 0:
        if input[i] >= input[i + 1]:
            print('*' * input[i], 'peak')
        else:
            print('*' * input[i])

    elif i == len(input) - 1: 
        if input[i] >= input[i - 1]:
            print('*' * input[i], 'peak')
        else:
            print('*' * input[i])

    elif input[i] >= input[i - 1] and input[i] >= input[i + 1]:
        print('*' * input[i], 'peak')

    else:
        print('*' * input[i])