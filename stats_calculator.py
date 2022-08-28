listk = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20, 33]

# Calculating the Mean of the above initiated list.

mean = sum(listk) / len(listk)
round(mean,2)

# Calculating the median based on above.

def median(listk):
    
    listk.sort()

    if len(listk) % 2 == 0:
        me = listk[len(listk)// 2]
        md = listk[len(listk) // 2 - 1]
        med = (me + md) / 2
    else:
        med = listk[len(listk)//2]
    print(med)
    
median(listk)


# Calculating the mode.

def mode(listk):
    # declaring a dictionary
    frequency = {}
    for i in listk:
        frequency.setdefault(i,0)
        frequency[i]+=1

    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
        elif j == 0:
            print("There's no mode")
        else:
            break
    print(mode)

    