'''Python String Method examples:'''


s = ‘hello’
print(s.capitalize())

#Output: Hello

s = ‘HELLO’
print(s.casefold())

#Output: hello

s = ‘hello’
print(s.centre(24, ‘#’))

#Output: ### hello ###

s = “code and code”
print(s.count(‘code’))

# Output: 2

s = “codeandcode”
print(s.endswith(‘code’))

#Output: True

s = “code and code”
print(s.find(‘and’))

#Output: 5

txt = "I can run {an:.2f} kilometers!"
print(txt.format(an = 8))

#Output: I can run 8.00 kilometers!

String =’hellocode’
print(string.index(‘llo’)

#Output: 2

s = “hello123”
print(s.isalnum())

#Output: True

s = “hello_123”
print(s.isalnum())

#Output: False

s = “hello”
print(s.isalpha())

#Output: True

s = “hello_123”
print(s.isalpha())

#Output: False

print(“123”.isdigit())

#Output: True
print(‘hello’.islower())

#Output: True
print(“1234”.isnumeric())

#Output: True

string = "\n\t\n"
print(string.isspace())

#Output True

string = 'code\nfirst\ngirls'
print( string.isspace())

#Output: False

string = "Hello"
print(string.istitle())

#Output: True

s = 'code First Girls'
print(s.istitle())

#Output: False
print((“HELLO”).isupper())

#Output: True


list = ['h', 'e', 'l', 'l', 'o']
print("".join(list))

#Output: hello


dict = {'hello': 1, 'coder': 2, 'girls': 3} 
s = '_'.join(dict)
print(s)

#Output: hello_coder_girls

s = 'CODE First Girls'
print(s.lower())

#Output: code first girls

s = "+-=*codefirstgirls"
print(s.lstrip("+-=*"))

#Output: codefirstgirls

s = 'Code First Girls'
print(s.replace(‘Girls’ ,’Queens’))

#Output: Code First Queens

string = "code/first/girls"
print(string.rsplit('/'))

#Output: [‘code’, ‘first’, ‘girls’]


string = "clairessss"
print(string.rstrip('s'))

#Output: claire

s = “Code, First, Girls”

print(s.split(‘,’))

#Output:  [‘Code’, ‘First’, ‘Girls’]

s = “Code\nFirst\nGirls\nDegree\nCourse”
print(s.splitlines())

#Output:[‘Code’, ‘First’, ‘Girls’, ‘Degree’, ‘Course’]
s = “Code First Girls”

print(s.startswith(‘Code’))
Print(s.startswith(‘The’))

#Output: True
        #False

s = “   code first girls  “
print(s.strip())

#Output: code first girls
#removes /n before and after

OR;

s= “the code first girls”
print(s.strip(‘the ‘)

#Output: code first girls

string = "CODE first GiRls" 
print(string.swapcase())

#Output: code FIRST gIrLs

string = "code first girls" 
print(string.swapcase())

#Output: Code First Girls

string = "Claire"
print(string.upper())

#Output: CLAIRE

'''Python List Methods Examples:'''

list =  [‘Code’, ‘First’, ‘Girls’]
print(list.append(‘Degree’))

#Output: Code First Girls Degree

list =  [‘Code’, ‘First’, ‘Girls’]
print(list.clear())

#Output []

list =  [‘Code’, ‘First’, ‘Girls’]
print(‘Copied list:’ list.copy())
#Output: Copied list: [‘Code’, ‘First’, ‘Girls’]

list =  [‘Code’, ‘First’, ‘Girls’]
print(list.count(‘Code’))

#Output: 1

list =  [‘Code’, ‘First’, ‘Girls’]
list.extend([‘Degree’, ‘Course’])
print(list)

#Output:  [‘Code’, ‘First’, ‘Girls’, ‘Degree’, ‘Course’]
list =  [‘Code’, ‘First’, ‘Girls’]
print(list.index(‘First’))

#Output: 1

list =  [‘Code’,  ‘Girls’]
print(list.insert(1, ‘First’))

#Output: [‘Code’, ‘First’, ‘Girls’]

list =  [‘Code’, ‘First’, ‘Girls’]
print(‘pop:’ ,list.pop())
print(‘list after pop:’, list)

#Output: pop: Girls

List after pop: [‘Code’, ‘First’]
list =  [‘Code’, ‘First’, ‘Girls’]
print(list.remove(‘Code’))

#Output: [‘First’, ‘Girls’]

list =  [‘Code’, ‘First’, ‘Girls’]

list =  [‘Code’, ‘First’, ‘Girls’]
print(list.reverse())

#Output: [‘Girls’, ‘First’, ‘Code’]

list =  [‘Code’, ‘Girls’, ‘First’]
print(list.sort())

#Output: [‘Code’, ‘First’, ‘Girls’]

'''Python Tuple Methods examples:'''

mytuple = (1, 2, 6, 8, 7, 5, 1, 6, 9, 5)

x = mytuple.count(5)
print(x)

#Output: 2

mytuple = (1, 2, 6, 8, 7, 5, 1, 6, 9, 5)

x = mytuple.index(8)
print(x)

#Output: 3

'''Python Dictionary Methods:'''

 d = {1: "code", 2: "first"}
 print( d.clear())

#Output :  {}

dict =  {1: ‘Code’, 2: ‘First’,3:  ‘Girls’}
print(‘Copied dict:’ , dict.copy())

#Output: Copied dict: {1: ‘Code’, 2: ‘First’,3:  ‘Girls’}

seq = ('a', 'b', 'c')
print(dict.fromkeys(seq, 1))

#Output: {'a': 1, 'b': 1, 'c': 1}

dict =  {1: ‘Code’, 2: ‘First’,3:  ‘Girls’}
print(dict.get(1))

#Output: Code

dict =  {‘A’: ‘Code’, ‘B’: ‘First’, ‘C’:  ‘Girls’}
print(dict.items())

#Output: dict_items([('A', 'Code'), ('B', 'First'), ('C', ‘Girls’)])

dict =  {‘A’: ‘Code’, ‘B’: ‘First’, ‘C’:  ‘Girls’}
print(dict.keys())

#Output: dict_keys(['A', 'B', 'C'])dict_keys(['A', 'B', 'C']

dict =  {‘A’: ‘Code’, ‘B’: ‘First’, ‘C’:  ‘Girls’}
print(dict.pop(‘First’))

#Output: {‘A’: ‘Code’,  ‘C’:  ‘Girls’}

d = {1: 'Code', 2: 'First', 3: 'Girls'}
print(d.popitem())

#Output: (3, 'Girls')

dict = {
  "Claire": "Blue",
  "Sandy": "Red",
  "Paul": “Yellow”
}
print(dict.setdefault("Paul", "Purple")


#Output: Yellow

dict = {
  "Claire": "Blue",
  "Sandy": "Red",
  "Paul": “Yellow”
}

print(dict.update({"Ann": "White"})

# Output: {
#   "Claire": "Blue",
#   "Sandy": "Red",
#   "Paul": “Yellow”,
#   "Ann": "White"}


dict = { 'Code':1, 'First':2, 'Girls':3}
print(dict.values())  

#Output: dict_values([1,2 , 3])

'''Python Set Methods:'''

set = {"code", "first", "girls"}
print(set.add(“degree”))

#Output:  {“degree”, "code", "first", "girls"}


set = {"code", "first", "girls"}
print(set.clear())

#Output: set()

set = {"code", "first", "girls"}
print(set.copy())

#Output:{"code", "first", "girls"}

set = {"code", "first", "girls"}
Set2 = {"code", "degree", "google"}

print(set.difference(set2))

#Output:  {"first", "girls"}

set = {"code", "first", "girls"}
Set2 = {"code", "degree", "google"}

print(set.intersection(set2))

#Output:  {"code"}

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
print(x.issubset(y))

#Output: True

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
print(x.issuperset(y))

#Output: True

set = {"code", "first", "girls"}
print(set.pop())

#Output: {"code", "girls"}

set = {"code", "first", "girls"}
print(set.remove( "first"))

#Output: {"code", "girls"}

set = {"code", "first", "girls"}
Set2 = {"code", "degree", "google"}

print(set.symmetric_difference(set2))

#Output:  {"first",  "degree", "google", "girls"}


set = {"code", "first", "girls"}
Set2 = {"code", "degree", "google"}

print(set.union(set2))

#Output:  {"code", "first",  "degree", "google", "girls"}

set = {"code", "first", "girls"}
Set2 = {"code", "degree", "google"}

print(set.update(set2))

#Output:  {"code", "first", "girls", "degree", "google"}

'''Python File Methods'''

f = open("myfile.txt", "r")
print(f.read())

#Output: The whole myfile.txt would open


f = open("myfile.txt", "r")
print(f.readline())

#Output: First line of myfile.txt file

f = open("myfile.txt", "r")

print(f.readlines())

#Output: [‘The whole myfile.txt would open’, ‘First line of myfile.txt file’]

f = open("myfile.txt", "a")
f.write("Please read me!")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())

# Output: The whole myfile.txt would open
# First line of myfile.txt 
# file
# Please read me!

f = open("myfile.txt", "a")
f.writelines(["Thank you for your time."])
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())

# Output: The whole myfile.txt would open
# First line of myfile.txt 
# file
# Please read me!
# Thank you for your time.


