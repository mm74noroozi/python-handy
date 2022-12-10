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
