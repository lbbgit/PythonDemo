import os

filename="hello.py"
print('hello，test os')
exec(open(filename).read())
#if os.path.isfile(filename)

    #if filename #and os.path.isfile(filename)
        #exec(open(filename).read())

filename2 = os.environ.get('PYTHONSTARTUP')
print(filename2)
print(os.environ.get('PATH'))

#execute
# if os.path.isfile('.hello.py')
#     execfile('.hello.py')
#
#     filename = os.environ.get('PYTHONSTARTUP')
#     if filename and os.path.isfile(filename):
#         exec (open(filename).read())

