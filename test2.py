arr1 = [1,1,0,0]
arr2 = [0,1,0,0]
  
for i in range(10):
    arrOUT = arr1[1:]+arr1[:1] # rotates array values of 1 digit
    arr1 = arr2
    arr2 = arrOUT
    print(arrOUT)
