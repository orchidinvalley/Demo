n=int(input('enter the number of students:'))
data = {}
subject=('physics','maths','history')
for i in range(0,n):
    name = input('enter the name of the student{} '.format(i+1))
    marks=[]
    for x in subject:
        marks.append(int(input('enter marks of {}'.format(x))))
    data[name]=marks
for x,y in data.items():
    total = sum(y)
    if total <120:
        print(x,'failed :(')
    else :
        print(x,'passed :)')

