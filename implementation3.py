input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1

steps=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

result=0

for step in steps:
    n_row=row+step[0]
    n_column=column+step[1]

    if n_row<=8 and n_column<=8 and n_row>=1 and n_column>=1:
        result+=1

print(result)