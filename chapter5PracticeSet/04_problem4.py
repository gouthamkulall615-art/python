s=set()
s.add(20)
s.add(20.0)
s.add('20')


print(len(s))
# we normally think we should get the 3 as the lenght butt the answer gives us two 

# because in the python 20 == 20.0 is same not different as set stores only unique elements we get length has two
