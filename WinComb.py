def win_comb(number:int = 3) -> list | set:
    a = [num for num in range(number**2)]
    result = []

    result.append(a[::(number+1)])
    result.append(a[number-1:number**2 - 1:number-1])

    for i in range(number):
        b = a[i*number: (number) + number*i]
        result.append(b)

    for j in range(number):
        b = a[j::number]
        result.append(b)
    
    result = [set(x) for x in result]

    return result
