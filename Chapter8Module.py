'''__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
'''
def functionOne():
    print('functionOne')

def functionTwo():
    print('functionTwo')

    
def functionThree():
    print('functionThree')
    return '3'