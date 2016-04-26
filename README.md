# Simple-Cryptography
* This is a small(currently) few pieces of code that preform rudimentary encryption and decryption sequences for an introductory class to cryptography
* Written in Python 3.5.1
* There will not be a version avilable for any version of Python lower than 3.5.1
* camelCase is the standard for variable declerations

##Overview
###File Crypto.py
* [Class map](#map)
* [Class caesar](#caesar)
* [Class afine](#afine)
* [Class viginere](#viginere)
* [Class viginereOld](#viginereOld)
* [Class cryptoErr](#cryptoErr)

###File Interface.py
* [Class task](#task)
* [Class choice](#choice)

##Class map
* Usage: `map(iterable,err = -1)`
	Takes an iterable and maps each item in the iterable to a number.You
	can then access item or number by calling the instance of the class on the item or
	number. It will return it's counterpart. If it fails to access, err will be returned
```pyhton	
myMap = map('abc0123)
mymap('0') #>>> 3
myMap(3) #>>> '0'
myMap('4') #>>> -1, the err is returned
```
* Property: `err`
	Is passed as an optional argument to the instance on initilization. Defaults to
	the value of -1 . This will be returned if an error occures. 
```python
myMap = map('abc')
myMap.err #>>> -1
myMapT = map('abc', err = 'My Error')
myMapT.err #>>> 'My Error'
```
* Method: `setMap(iterable)`
	Allows the instance of the class to have it's character map redefined
```python
myMap = map('abc')
myMap.setMap('efg')
myMap.mapI #>>> 'efg'
```
