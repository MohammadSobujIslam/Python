# set learning
set_lirn={'sobuj','nipa','july','sathi',12,34}
print(set_lirn)
for x in set_lirn:
    print(x)

print('sobuj mia' in set_lirn)    
print(34 in set_lirn)   
set_lirn.add(44)
set_lirn.add('taslima akter')
set_lirn.add('she loves razib hasan')
set_lirn.update([1,1,2,4,6,7,3993,'sobuj mia'])
list=[1,'jweel','washik','aakil','milton','anik','ami tumra']
set_lirn.update(list)
set_lirn.update([99])
print(f"This set length =  {len(set_lirn)}")

set_lirn.remove(99)
set_lirn.remove(3993)
set_lirn.discard(2)
var=set_lirn.pop()
#set_lirn.clear()
print(var)
#del set_lirn
print(set_lirn)
print("\n\n")
set1={1,3,5,6}
set2={'sobuj','razib','shanto','shohag'}
union_set=set1.union(set2)
print(union_set)
set2=set2.union(set1)
print(set2)
set_costructor=set((1,3,55,66,'hi'))
print(set_costructor)

