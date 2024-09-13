Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("列表知识点整理！")
列表知识点整理！
>>> players = ["Fly","Hurt","Cat","Gemini","Yang"]
>>> players
['Fly', 'Hurt', 'Cat', 'Gemini', 'Yang']
>>>  print("依次访问元素：")
 
SyntaxError: unexpected indent
>>> for each in players:
	print(each)

	
Fly
Hurt
Cat
Gemini
Yang
>>> players[0]
'Fly'
>>> players[len(players)-1]
'Yang'
>>> players[-1]
'Yang'
>>> players[0:3]
['Fly', 'Hurt', 'Cat']
>>> players[3:6]
['Gemini', 'Yang']
>>> players[:]
['Fly', 'Hurt', 'Cat', 'Gemini', 'Yang']
>>> players[0:6:2]
['Fly', 'Cat', 'Yang']
>>> players[::2]
['Fly', 'Cat', 'Yang']
>>> players[6:0:-1]
['Yang', 'Gemini', 'Cat', 'Hurt']
>>> players
['Fly', 'Hurt', 'Cat', 'Gemini', 'Yang']
>>> players[4:0:-1]
['Yang', 'Gemini', 'Cat', 'Hurt']
>>> players[::-1]
['Yang', 'Gemini', 'Cat', 'Hurt', 'Fly']
>>> players[5:0:-1]
['Yang', 'Gemini', 'Cat', 'Hurt']
>>> players[4:-1:-1]
[]
>>> players[::1]
['Fly', 'Hurt', 'Cat', 'Gemini', 'Yang']
>>> players[::-1]
['Yang', 'Gemini', 'Cat', 'Hurt', 'Fly']
>>> print("增！")
增！
>>> players.append("Jiucheng")
>>> players
['Fly', 'Hurt', 'Cat', 'Gemini', 'Yang', 'Jiucheng']
>>> players.extend("Jiuzhe","fuzhuanghao")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    players.extend("Jiuzhe","fuzhuanghao")
TypeError: extend() takes exactly one argument (2 given)
>>> players.extend(["Jiuzhe","fuzhuanghao"])
>>> players
['Fly', 'Hurt', 'Cat', 'Gemini', 'Yang', 'Jiucheng', 'Jiuzhe', 'fuzhuanghao']
>>> print("删！")
删！
>>> players.remove("fuzhuanghao")
>>> players
['Fly', 'Hurt', 'Cat', 'Gemini', 'Yang', 'Jiucheng', 'Jiuzhe']
>>> players.pop("Jiuzhe")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    players.pop("Jiuzhe")
TypeError: 'str' object cannot be interpreted as an integer
>>> players.pop(6)
'Jiuzhe'
>>> players
['Fly', 'Hurt', 'Cat', 'Gemini', 'Yang', 'Jiucheng']
>>> players.pop(3)
'Gemini'
>>> players
['Fly', 'Hurt', 'Cat', 'Yang', 'Jiucheng']
>>> players.insert(0,"Gemini")
>>> players
['Gemini', 'Fly', 'Hurt', 'Cat', 'Yang', 'Jiucheng']
>>> players.pop(len(players)-1)
'Jiucheng'
>>> players
['Gemini', 'Fly', 'Hurt', 'Cat', 'Yang']
>>> players.clear()
>>> players
[]
>>> print("改！")
改！
>>>  players = ["Fly","Hurt","Cat","Gemini","Yang"]
 
SyntaxError: unexpected indent
>>> players = ["Fly","Hurt","Cat","Gemini","Yang"]
>>> players[3] = "鹌鹑"
>>> players
['Fly', 'Hurt', 'Cat', '鹌鹑', 'Yang']
>>> 