for i in range(19): 
    if i >= 10:
        if i != 18:   
            print(f"{10 - i % 10},", end='')
        else:
            print(f"{9 - i % 10}")
    else:
        print(f"{i +1},", end='')
