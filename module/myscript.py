# import順番：標準ライブラリ、サードパーテーのライブラリ、自分たちのライブラリ、ローカルのライブラリ

import sys
sys.path.append("/Users/anne/Desktop/PythonLecture/function/")
import docstring  # ↑appendした後にimport
# import mymodule
import mymodule as mm

from mymodule import my_func, another_func
# from mymodule import *  # _関数名は呼び出せない


# mymodule.my_func()
mm.my_func()

my_func()
another_func()

print(sys.path)
print(docstring.multiply(3, 4))