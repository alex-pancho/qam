a = int (8000) # километров до следующего ТО
b = int (5000) # миль до следующего ТО
e = str ("incorrect data")
x = str ("следующие ТО на пробеге ")
input_1 = input ("укажите меру измерения 1-км, 2-mille ")
if  (input_1) == "1":
    millaege_KM = input("введите пробег на последнем ТО ")
    c = int (millaege_KM)
    result = a + c
if  (input_1) == "2":
    millaege_MI = input("введите пробег на последнем ТО ")
    d = int (millaege_MI)
    result = b + d
if (input_1) > "2":
    e = str ("incorrect data")
    result = e 
if (input_1) < "1":
    e = str ("incorrect data")
    result = e
print (x) 
print (result)