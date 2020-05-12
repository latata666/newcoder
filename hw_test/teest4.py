f = open('users.txt', 'a+') #清空文件内容再写
f.write('aaa') #只能写字符串
f.write('\n')
f.writelines(['123','\n', 'bbb','\n']) #可写所有能迭代的类型，例如list
f.writelines(('456','\n', 'ccc')) #例如tuple
f.close()