import ctypes
dll = ctypes.windll.LoadLibrary( 'test.dll' )
import ctypes
dll = ctypes.WinDll( 'test.dll' )
#其中ctypes.windll为ctypes.WinDll类的一个对象，已经在ctypes模块中定义好的。在test.dll中有test接口，可直接用dll调用即可
nRst = dll.test( )
print(nRst)