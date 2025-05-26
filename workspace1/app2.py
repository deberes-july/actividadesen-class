


##Hello

myDictionary={'cat':'cute','dog':'friend','donkey':'hard-working'}
print(myDictionary['donkey'])


print('cat' in myDictionary)

myDictionary['fish']='wet'

for key in myDictionary:
    feature=myDictionary[key]
    print('The %s is %s '%(key,feature))

for key, value in myDictionary.items():
    print('The %s is %s ' %(key, value))



print('*************************')

#dictionary={'1':1, '2':4........}

myDictionary1={i:i**2 for   i in range(20)}
print(myDictionary1)
##lista = [{str(i): i**2} for i in range(1, 20)]
# print("\n".join([f"{str(i)}: {i**2}" for i in range(1, 20)]))


##CONTENERDOR SETprint("\n".join([f"{str(i)}: {i**2}" for i in range(1, 20)]))

print('SET CONTAINER')
animals={'cat','dog','chicken','hen','monkey'}
print('fish' in animals)
animals.add('fish')
print(animals)
animals.add('mouse')
print(animals)


numberOfElements=len(animals)
print(numberOfElements)


animals.remove('cat')
print(animals)
print(type(animals))
print(len(animals))


print('**TUPLES****')
tupleData=(5,15,5)
print(type(tupleData))

print('**ELIMINAR***')

aux=list(tupleData)
aux.remove(15)
tupleData=tuple(aux)
print(tupleData)

# tupleData = tupleData[:1] + tupleData[2:]
# print(tupleData)


# print('***AGREGAR****')
# tupleData = tupleData + (10,)
# print(tupleData)

