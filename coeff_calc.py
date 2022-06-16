

print("Coefficient calculation")


"""
points = 11
t=[0.0000000000000000000000000000000, 
0.0000000107000000001793000000000,
0.0000000203000000002004000000000,
0.0000000304999999999923000000000,
0.0000000501999999999881000000000,
0.0000000610000000002015000000000,
0.0000000801000000002095000000000,
0.0000005308000000001610000000000,
0.0000006916999999999510000000000,
0.0000008399000000001810000000000,
0.0000008506999999999610000000000]

v=[-0.00783818720000,
0.00331806260000,
0.00554589510000,
0.00413555560000,
0.00636237800000,
-0.00380059150000,
-0.00098923689000,
-0.00039601058000,
-0.00153832530000,
-0.00355399110000,
-0.00521862950000]
"""
t = []
v = []
x = []
y = []
m = []
b = []

PHI = 3.1415926535
CONST1 = 0.0

op_user = True

if op_user == True:
    points = input("Enter number of points: ")


    for i in range (int(points)):
        val = float(input("Enter Time %s: " %(i)))
        t.append(val)
        val = float(input("Enter Voltage %s: " %(i)))
        v.append(val)

#print("Printing t and v")
#print(t)    
#print(v)

CONST1 = PHI / t[-1]

for i in range (int(points)):
    x.append(t[i]*CONST1)
    y.append(v[i])

#print("Printing x and y")
#print(x)    
#print(y)

for i in range (int(points)-1):
    m.append( (y[i+1]-y[i])/(x[i+1]-x[i]) )

for i in range (int(points)-1):
    b.append( y[i+1] - m[i]*x[i+1] )
    

#print("Printing m")
#print(m)
#print("Printing b")
#print(b)

with open('coeff.txt', 'w') as f:

    for i in range (int(points)-1):
        
        if b[i]<0:
            sign = ''
        else:
            sign = '+'

        mystring = ','+'{'+str(m[i])+'x'+sign+str(b[i])+','+str(x[i])+'<'+'x'+'<'+str(x[i+1])+'}\n'
        f.write(mystring) 
        print (mystring)
        mystring = ''
        sign = ''