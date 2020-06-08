"""class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)



h = Hello()
h.hello()
print(type(Hello))
print(type(h))



def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello',(object,),dict(hello=fn))

h = Hello()
h.hello()
print(type(Hello))

print(type(h))
"""



# # metaclass是类的模板，所以必须从`type`类型派生：
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
# class MyList(list, metaclass=ListMetaclass):
#     pass
#
# L = MyList()
# L.add(1)
# print(L)
# L2 = list()
# L2.add(1)




class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)