#字典dictionary的用法,dict={}，键(key) : 值(value)
dict={} #字典需要提前标识，创建空字典使用 { }
dict['one'] = "1 - 菜鸟教程" #dict[对象，可以是字符串，也可以是数字]=值(value)
tinydict = {'name': 'runoob','code':1, 'site': '123'}

print (dict['one'])       # 输出键为 'one' 的值
print(tinydict) # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

#1 - 菜鸟教程
#{'name': 'runoob', 'code': 1, 'site': '123'}
#dict_keys(['name', 'code', 'site'])
#dict_values(['runoob', 1, '123'])




