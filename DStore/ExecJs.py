import execjs
import os
execjs.eval("'red yellow blue'.split(' ')") #['red', 'yellow', 'blue']
ctx = execjs.compile("""
     function add(x, y) {
         return x + y;
     }
""")
ctx.call("add", 1, 2) #3



execjs.get().name # this value is depends on your environment.
os.environ["EXECJS_RUNTIME"] = "Node"
execjs.get().name #'Node.js (V8)'

#You can choose JavaScript runtime by execjs.get():
import execjs.runtime_names
import execjs.runtime_names
default = execjs.get()  
jscript = execjs.get(execjs.runtime_names.JScript)
node___ = execjs.get(execjs.runtime_names.Node)
default.eval("1 + 2") #3
jscript.eval("1 + 2") #3
node___.eval("1 + 2") #3



