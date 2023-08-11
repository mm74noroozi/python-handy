# python-handy
## python serve path
```bash
python -m http.server
```
## leading zeros
```python
>>> f"{329:05d}"
00329
```
## formatter
```python
>>> f"Hey {name}, there's a {errno:#x} error!"
"Hey Bob, there's a 0xbadc0ffee error!"
>>> from string import Template
>>> t = Template('Hey, $name!')
>>> t.substitute(name=name)
'Hey, Bob!'
```
## websocket client
```bash
python -m websockets <uri>
```
## PyYaml
```python
import yaml

data = yaml.load(fp,yaml.SafeLoader)
yaml.dump(data,new_fp,yaml.SafeLoader)
```
## LifoQueue
```python
>>> from queue import LifoQueue
>>> s = LifoQueue()
>>> s.put('eat')
>>> s.get()
'eat'
>>> s.get_nowait()
queue.Empty
>>> s.get()
# Blocks / waits forever...
```
## Heap
```python
import heapq

myHeap = [3, 1, 5]

heapq.heapify(myHeap) # make a heap with elements of (myHeap = [3, 1, 5]) and store it in myHeap
heapq.heappush(myHeap, -5) # add -5 to myHeap
minElement =  heapq.heappop(myHeap)  # pop min element in myHeap and return value of min elemnt

print(minElement) # print -5
```
## FIFO
```python
>>> from multiprocessing import Queue
>>> q = Queue()
>>> q.put('eat')
>>> q.get()
'eat'
>>> q.get()
'sleep'
>>> q.get()
'code'
>>> q.get()
# Blocks / waits forever...
```
## priority queue
uses heap and also supports multiprocessing
```python
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))
while not q.empty():
  next_item = q.get()
  print(next_item)
# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')
```
## lambda function -> operator module
```
import operator
lambda x:x[1] -> operator.itemgetter(1)
lambda x,y:x+y -> operator.add
```
## interesting hash!
```python
>>> hash(987)
987
>>> hash(True)
1
>>> hash('salam')
1248647572205467951
>>> hash('salam0')
-2263522201675412136
```
## args and kwargs
```python 
>>> a = [1,2,3]
>>> b = [4,5]
>>> print([*a,*b])
[1, 2, 3, 4, 5]
>>> dict1 = {'a':1,'b':2}
>>> dict2 = {'c':0}
>>> print({**dict1,**dict2}
{'a': 1, 'b': 2, 'c': 0}
```
## advance disassamble 
```python
>>> def greet(name):
>>>   return 'Hello, ' + name + '!'

>>> greet.__code__.co_code
b'dx01|x00x17x00dx02x17x00Sx00'
>>> greet.__code__.co_consts
(None, 'Hello, ', '!')
>>> greet.__code__.co_varnames
('name',)

>>> import dis
>>> dis.dis(greet)
2 0 LOAD_CONST 1 ('Hello, ')
2 LOAD_FAST 0 (name)
4 BINARY_ADD
6 LOAD_CONST 2 ('!')
8 BINARY_ADD
10 RETURN_VALUE
```
## bitwise operations on datatypes
```python
>>> x = 3
>>> y = 4
>>> x or y
3
>>> x and y
4
```
## python set operations
```python
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
{1, 2, 3, 4, 5} & {3, 4, 5, 6} # {3, 4, 5}
# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6}) # {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5} | {3, 4, 5, 6} # {1, 2, 3, 4, 5, 6}
# Difference
{1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
{1, 2, 3, 4} - {2, 3, 5} # {1, 4}
# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5} # {1, 4, 5}
# Superset check
{1, 2}.issuperset({1, 2, 3}) # False
{1, 2} >= {1, 2, 3} # False
# Subset check
{1, 2}.issubset({1, 2, 3}) # True
{1, 2} <= {1, 2, 3} # True
# Disjoint check
{1, 2}.isdisjoint({3, 4}) # True
{1, 2}.isdisjoint({1, 4}) # False
# Add and Remove
s = {1,2,3}
s.add(4) # s == {1,2,3,4}
s.discard(3) # s == {1,2,4}
s.discard(5) # s == {1,2,4}
s.remove(2) # s == {1,4}
s.remove(2) # KeyError!
```
## Counter
```python
>>> from collections import Counter
>>> counterA = Counter(['a','b','b','c'])
>>> counterA
Counter({'b': 2, 'a': 1, 'c': 1})
>>> counterA.most_common(1)
[('b',2)]
>>> a = Counter(words)
>>> b = Counter(morewords)
>>> a
Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
 "you're": 1, "don't": 1, 'under': 1, 'not': 1})
>>> b
Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
 'my': 1, 'why': 1})
>>> # Combine counts
>>> c = a + b
>>> c
Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
 'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
 'looking': 1, 'are': 1, 'under': 1, 'you': 1})
>>> # Subtract counts
>>> d = a - b
>>> d
Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
 "you're": 1, "don't": 1, 'under': 1})
```
## max length queue
```python
>>> q = deque(maxlen=3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(4)
>>> q
deque([2, 3, 4], maxlen=3)
>>> q.append(5)
>>> q
deque([3, 4, 5], maxlen=3)
```
## finding n largets or smalest items in queue
```python
import heapq
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
```
## defaultdict
```python
from collections import defaultdict

d = defaultdict(lambda :2)
d[1] # 2
```
## slice
```python
record = '....................100 .......513.25 ..........'
SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])
```
## filtering based on other sequence
```python
addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

>>> from itertools import compress
>>> more5 = [n > 5 for n in counts]
>>> more5
[False, False, True, False, False, True, True, False]
>>> list(compress(addresses, more5))
['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
```
## combine dicts
```python
from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)
```
## fnmatch
```python
>>> from fnmatch import fnmatch, fnmatchcase
>>> fnmatch('foo.txt', '*.txt')
True
>>> fnmatch('foo.txt', '?oo.txt')
True
>>> fnmatch('Dat45.csv', 'Dat[0-9]*')
True
>>> # On OS X (Mac)
>>> fnmatch('foo.txt', '*.TXT')
False
>>> # On Windows
>>> fnmatch('foo.txt', '*.TXT')
True
>>> fnmatchcase('foo.txt', '*.TXT')
False
```
## regex
```python
>>> import re
>>> datepat = re.compile(r'\d+/\d+/\d+')
>>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> datepat.findall(text)
['11/27/2012', '3/13/2013']
>>> datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
>>> datepat.findall(text)
[('11', '27', '2012'), ('3', '13', '2013')]
>>> m =  datepat.match('11/27/2012') # only first item
>>> for m in datepat.finditer(text):
    ... print(m.groups()) # 11/27/2022 ...
    ... print(m.group())  # ('11', '27', '2012')
>>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2012-11-27. PyCon starts 2013-3-13.'
>>> newtext, n = datepat.subn(r'\3-\1-\2', text)
>>> newtext
'Today is 2012-11-27. PyCon starts 2013-3-13.'
>>> n
2
>>> re.findall('python', text, flags=re.IGNORECASE)
>>> re.sub('python', 'snake', text, flags=re.IGNORECASE)
```
In regular expressions (regex), the .* pattern matches any character (except for a newline character) zero or more times.

Here's a breakdown of what .* means:

    . matches any single character except for a newline character.
    * matches the preceding character or group zero or more times.

So, .* matches any sequence of characters, including an empty string. For example, the regex pattern a.*b would match any string that starts with an "a", ends with a "b", and has any characters in between.

Note that .* is a greedy pattern, which means it will match as much as possible. If you want to match as little as possible, you can use the non-greedy version .*?
```python
>>> str_pat = re.compile(r'\"(.*)\"')
>>> text2 = 'Computer says "no." Phone says "yes."'
>>> str_pat.findall(text2)
['no." Phone says "yes.']
>>> >>> str_pat = re.compile(r'\"(.*?)\"')
>>> str_pat.findall(text2)
['no.', 'yes.']
```
multiline match
```python
>>> comment = re.compile(r'/\*(.*?)\*/')
>>> text2 = '''/* this is a
    ... multiline comment */
    ... '''
>>> comment.findall(text2)
[]
>>> comment = re.compile(r'/\*((?:.|\n)*?)\*/')
>>> comment.findall(text2)
[' this is a\n multiline comment ']
>>> comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
>>> comment.findall(text2)
[' this is a\n multiline comment ']
```
## translate
```python
>>> s = 'pýtĥöñ\fis\tawesome\r\n'
>>> s
'pýtĥöñ\x0cis\tawesome\r\n'
>>> remap = {
... ord('\t') : ' ',
... ord('\f') : ' ',
... ord('\r') : None # Deleted
... }
>>> a = s.translate(remap)
>>> a
'pýtĥöñ is awesome\n'
```
## text centering
```python
>>> text = 'Hello World'
>>> text.center(20,'*')
'****Hello World*****'
>>> format(text, '*^20s')
'****Hello World*****'
```
## vars vs locals
```python
class Example:
    def __init__(self):
        self.x = 1
        self.y = 2

ex = Example()
print(vars(ex))  # {'x': 1, 'y': 2}
def example_func():
    a = 1
    b = 2
    print(locals()) # {'a': 1, 'b': 2}

example_func()
```
## format_map
```python
>>> class Info:
... def __init__(self, name, n):
... self.name = name
... self.n = n
...
>>> a = Info('Guido',37)
>>> s.format_map(vars(a))
'Guido has 37 messages.'
```
## __missing__
```python
class safesub(dict):
  def __missing__(self, key):
  return '{' + key + '}'
>>> del n # Make sure n is undefined
>>> s.format_map(safesub(vars()))
'Guido has {n} messages.'
```
