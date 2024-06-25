# RunThisCode
# print(' '.join(("Let's", "Start", "Exercises" )))



#1 find sigle element in tuple
#tup = (1 , 1 , 2 , 3 , 2 , 2 , 1)
#counts={}
#for elem in tup:
#    if elem in counts:
#        counts[elem]+=1
#    else:
#        counts[elem]=1
#signle_element=[key for key,value in counts.items()if value==1]
#print(signle_element)        


#2 find sum of diagonal elements 
#tup = ((1, 2, 3),
#       (4, 5, 6),
#       (7, 8, 9))
#sum_diagonal=tup[0][0]+tup[1][1]+tup[2][2]
#print (sum_diagonal)

#3 you have one input(n), remove nth element from tuple. otherwise print error
#tup = (1 , 2 , 7 , 4,  2,  3, 8 , 9 , 10 , 20)
#n = int(input('Enter n: '))
#if 0<=n<len(tup):
#    new_tup=tup[:n]+tup[n+1:]
#    print(new_tup)
#else:
#    print("Error index out of range")
#4 calculate product of all elements in tuple
#tup = (1 , 2 , 7 , 4,  2,  3, 8 , 9 , 10 , 20)
#product=1
#for num in tup:
#    product*=num
#    print("Product of all elements in the tuple:",product)
# you have 2 inputs n and m. reshape tuple to 2d array with n x m size.
#x = eval(input('Enter a tuple: '))
#print("Original tuple:", x)
#n = int(input("Enter the number of rows (n): "))
#m = int(input("Enter the number of columns (m): "))
#if n * m != len(x):
#    print("Error: Tuple size does not match the specified dimensions.")
#else:
#    two_d_array = []
#    for i in range(0, len(x), m):
#        two_d_array.append(x[i:i+m])
#    print("2D array of size", n, "x", m, ":")
#    for row in two_d_array:
#        print(row)
