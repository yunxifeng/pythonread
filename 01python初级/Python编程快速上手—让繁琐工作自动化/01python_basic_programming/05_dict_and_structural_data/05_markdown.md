# 笔记
1.三个dict方法: keys(), values(), items()
2.get()方法
    - 两个参数:
        - 键
        - 备用值
3.setdefault()方法
    - 为某个键设置默认值,当该键没有任何值时使用它
    -两个参数:
        - 要检查的键
        - 如果该键不存在时要设置的值
    - 如果该键确实存在,方法就会返回键的值,如果该键不存在,返回设置的默认值
4.漂亮打印
- import pprint
    - 函数pprint(): 干净有序
    - 函数pformat(): 如果希望得到漂亮打印的文本作为字符串， 而不是显示在屏幕上， 那就调用pprint.pformat()。
# 习题
1.d = {}
2.{"fow": 42}
!!!3.保存在字典中的项是无序的，而列表中的项是有序的
4.KeyError
5.没有区别。 in 操作符检查一个值是不是字典中的一个键。
6. 'cat' in spam 检查字典中是不是有一个 'cat' 键，而'cat' in spam.values() 检查是
    否有一个值 'cat' 对应于 spam 中的某个键。
7.spam.setdefault("color", black)
8.pprint模块, pprint()函数和pformat()函数
实践
05--p02.py
