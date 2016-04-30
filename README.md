# Simple-Cryptography
* This is a small(currently) few pieces of code that preform rudimentary encryption and decryption sequences for an introductory class to cryptography
* Written in Python 3.5.1
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

##Class `map`
#####Usage: `map(iterable,err = -1)`
* Takes an iterable and maps each item in the iterable to a number.You
can then access item or number by calling the instance of the class on the item or
number. It will return it's counterpart. If it fails to access, err will be returned
```pyhton	
myMap = map('abc0123)
mymap('0') #>>> 3
myMap(3) #>>> '0'
myMap('4') #>>> -1, the err is returned
```
* For maps that use escaped keys  be sure that it is made with the proper escape key
sequence according to Python 3.5.1 , see the example below
```python
#incorect
myMap = map('\') 
myMap('\') #>>> Returns the map's err value
myMap(0) #>>> Returns the map's err value
#correct
myMap = map('\\') 
myMap('\\') #>>> Returns 0
myMap(0) #>>> Returns '\\' 
```
#####Property: `err`

* Is passed as an optional argument to the instance on initilization. Defaults to
the value of -1 . This will be returned if an error occures. 
```python
myMap = map('abc')
myMap.err #>>> -1
myMapT = map('abc', err = 'My Error')
myMapT.err #>>> 'My Error'
```
#####Property: `mod`

* Is where the modulo value for the map is stored. 
```python
myMap = map('abc')
myMap.mod #>>> 3
```
#####Property: `mapI`

* Where the iterable (other known as the character map string) is stored.
Do not access this property directly! use the method `setMap()` 
```python
myMap = map('abc')
myMap.mapI #>>> 'abc'
```
#####Method: `setMap(iterable)`

* Allows the instance of the class to have it's character map redefined
```python
myMap = map('abc')
myMap.setMap('efg')
myMap.mapI #>>> 'efg'
```
## Class `caesar`
#####Usage: `caesar()`

* Contains methods tools and letter sequences usefull for Caesar Ciphers.
One thing specific to this class is it's value for the property
`cipherType #>>> 'caesar'` for more info refer to the documentation on this property.
```python
c = caesar()
c.decrypt('bcd',1) #>>> returns 'abc'
```
#####Property: `cipherType`

* This returns the cipher's name that the class is for
as a lowercase string of the name without spaces if there are any.
```python
c = caesar()
c.cipherType #>>> 'caesar'
```
#####Property: `defMap`

* This is where the default map used in the class is stored. Whenever a function 
in the class needs a map it uses this property. The default map with it's initilized 
character set is as follows: `map(abcdefhijklmnopqrstuvwxyz)`
```python
c = caesar()
c.defMap #>>> Is the map instance object
```
#####Method: `numToChr(intiger,forceMap = False)`

* This method maps an intiger number to it's corresponding string value.
By default it uses the `defMap` but a instance of map can be passed to it as an 
optional argument that will overide `defMap`. For more info on maps see documentation
Class `map`.
```python
c = caesar()
c.numToChr(0) #>>> 'a'
```
#####Method: `chrToNum(string,forceMap = False)`

* This method maps an string value and returns it's corresponding intiger number.
By default it uses the `defMap` but a instance of map can be passed to it as an 
optional argument that will overide `defMap`. It is the counterpart to the method `numToChr()`
For more info on maps see documentation Class `map`.  
```python
c = caesar()
c.chrToNum('a') #>>> 0
```
#####Method: `encrypt(string,intiger)`

* Encrypts the string based upon the intiger which it the key for encryption.
It uses the `defMap` for encryption. It encrypts according to the classical 
definition of a Caesar Cipher.
```python
c = caesar()
c.encrypt('abc',1) #>>> 'bcd'
```
#####Method: `decrypt(string,intiger)`

* Decrypts the string based upon the intiger which it the key for decryption.
It uses the `defMap` for decryption. It decrypts according to the classical 
definition of a Caesar Cipher.
```python
c = caesar()
c.decrypt('bcd',1) #>>> 'abc'
```
#####Method: `opp(bool)`

* Reverses the bolean value.
```python
opp(True) #>>> False
opp(False) #>>> True
```
#####Method: `setMap(object)`

* Sets the value of the `defMap` to the map instance
it is given. Do not get this confused with the `setMap()` 
method of the Class `map`. To be fixed in a future Update
```python
myMap = map('abc')
c = caesar()
c.setMap(myMap)#Caesar will now use this map by default
```
#####Method: `az(string)`

* Takes a single letter or character that is a string
and tests if it is a lowercase letter abc...z. Use this
like an asertion test. 
```python
c = caesar()
c.az('a') #>>> True
c.az('A') #>>> False
```
#####Method: `sanitizeMsg(string,string)`

* The first argument is the message and the second is the
characters that will be removed from the message.
```python
c = caesar()
c.sanitizeMsg('aabaa','b') #>>> 'aaaa'
```
#####Method: `frequencyAnalysis(string)`

* Gets the frequency of each unique letter in the string and 
returns a list of percentages where the percentage of a certin
character is the is the list item at the map instance coresponding
value. Any character not found in the map instance used will be removed.
```python
c = caesar()
c.frequencyAnalysis('aaaab') #>>> [0.8,0.2]
```
#####Method: `variance(iterable)`

* Returns the standard Deviation of the iterable(must be a frequency list) from
that of normal english and returns that number as a float. Only works when the map instance
is `map('abcdefhijklmnopqrstuvwxyz')`
```python
c = caesar()
c.variance('aaaeeeettt') #>>> [0.3, 0.0, 0.0, 0.0, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```
#####Method: `noKeysDecrypt(string)`

* Runs through all the possible keys and checks the decrypted message's 
variance from that of normal english and returns the corectly decrypted message 
and the key used to do it in a list. Only works when the map instance is `map('abcdefhijklmnopqrstuvwxyz')`
```python
c = caesar()
c.nokeysDecrypt('b') #>>> will return the most plausable decryption ['a',1]
```
