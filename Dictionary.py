
dictt={
    'year':2020,
    'language':'Python',
    'version':3.8
    

}
dictionnary_dict={
    'name':'mohammad sobuj',
    'age':22,
    'identity':'university student',
    'department':'CSE',
    'birth_day':1998,
    'dict': {
    'year':2020,
    'language':'Python',
    'version':3.8
    

       },
    
}
dictionnary_dict['age']=23
dictionnary_dict['program']="learnner"

print(dictionnary_dict)
print(dictionnary_dict['age'])
print(dictionnary_dict.get('name'))
print(dictionnary_dict.get('identity'))

for dic in dictionnary_dict:
    print(dic)
print('\n...Now value....\n\n')    
for value in dictionnary_dict:    
    print(dictionnary_dict[value])
print('\n...Now value....\n\n')  

for z in dictionnary_dict.values():
    print(z)

for m,n in dictionnary_dict.items():
    print(f"{m , n}")   


if 'name' in dictionnary_dict:
    print('this value is exist')    

print(len(dictionnary_dict)) 


dict1=dictionnary_dict.copy()
dir=dict(dictt)
print(dir)
print(dict1)
con_dict=dict(brand='apple',price=100000,model='I phone X',counry='america')
#con_dict.popitem()
print(con_dict)


a=4
b=44
print('A is a small value') if a>b else print('b is a large value')
print("A") if a > b else print("=") if a == b else print("B")
phone=input("phone: ")

digit_map={
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'four'
}
output=""
for char in phone:
    output+=digit_map.get(char,'!')+' '
print(output) 