'''
程序：循环的嵌套，双重循环
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print('*', end='')
        j = j + 1
    print()
    i = i + 1
