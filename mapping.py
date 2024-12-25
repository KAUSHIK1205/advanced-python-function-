l1=(1,2,3,4,5,6,7,8,9)
l2=(9,8,7,6,5,4,3,2,1)
l3= map (lambda x,y :x+y, l1,l2)
print(list(l3))

def cube_number(x):
    return x*x*x
l4=[1,2,3]
result=map(cube_number,l4)
print(list(result))