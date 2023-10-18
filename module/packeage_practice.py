# import myfirstpapackeage.module1
# from myfirstpapackeage.subdir.module2 import myfunc
# from myfirstpapackeage.module1 import myfunc
import myfirstpapackeage.subdir.module2
from myfirstpapackeage.subdir import *

myfunc()
myfirstpapackeage.myfunc()
myfirstpapackeage.subdir.module2.myfunc2()