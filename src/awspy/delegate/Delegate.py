class Delegate:
     def __init__(self, *calls, **opts):
         for call in calls:
             if not callable(call):
                 raise RuntimeError, str(call) + ' not a callable object'
         self.calls = () + calls
         self.emptyExcept = opts.get('emptyExcept', False)
         self.proto = opts.get('proto')
     def __call__(self, *args, **kwargs):
         if self.emptyExcept and not self.calls:
             raise RuntimeError, 'No callable objects'
 
         try:
             result = None
             for call in self.calls:
                 result = call (*args, **kwargs)
             return result
         except TypeError:
             raise RuntimeError, 'Invalid callable type: ' + str(call)
 
     def __add__(self, call):
         if not callable(call):
             raise RuntimeError, str(call) + ' not a callable object'
         return delegate(*(self.calls + (call,)))
 
     def __iadd__(self, *calls):
         self.calls += calls
         return self
 
     def __sub__(self, call):
         return delegate (*[x for x in self.calls if x != call])
 
     def __isub__(self, call):
         self.calls = tuple([x for x in self.calls if x != call])
         return self
 
     def __str__(self):
         if self.proto:
             return '<delegate object, proto type: %s>' % repr(self.proto)
         return repr(self)
 
     def clear (self):
         self.calls = []
 
     def bind (self, call):
         self.__iadd__(call)
 
     def unbind (self, call):
         if call not in self.calls:
             raise RuntimeError, str(call) + ' not bind'
         self.calls = tuple ([x for x in self.calls if x != call])
         
         
'''       
if __name__ == '__main__':
     def a(v1, v2, **kwargs):
         print '\ta:', v1, v2
     def b(*args, **kwargs):
         print '\tb:', args, kwargs
     def c(v1, v2, **kwargs):
         print '\tc:', v1, v2, 'hello=', kwargs.get('hello')
 
     class Test:
         def hello(self, v1, v2, **kwargs):
             print '\tTest.hello:', v1, v2
 
     class Test1:
         def __call__(self, v1, v2, **kwargs):
             print '\tTest1.__call__:', v1, v2
 
     print '======== test delegate.__init__ and delegate.__call__'
     print '\t==== a, b, c, Test.hello, Test1'
     f = delegate(a, b, c, Test().hello, Test1())
     f (3, 4, hello='world')
     print '======== test delegate.__add__'
     print '\t==== a, b, c, Test.hello, Test1, a'
     f1 = f + a
     f1 (5, 6)
     print '======== test delegate.__iadd__'
     print '\t==== a, b'
     f2 = delegate(a, b)
     f2 (3, 7)
     print '\t==== a, b, c'
     f2 += c
     f2 (9, 10)
     print '======== test delegate.__sub__'
     print '\t==== a, b, c'
     f3 = delegate (a, b, c)
     f3 (11,11)
     print '\t==== b, c'
     f3 = f3 - a
     f3 (13, 13)
     print '\t==== b'
     f3 = f3 - c
     f3 (15, 15)
     print '======== test delegate.__isub__'
     print '\t==== a, b, c'
     f4 = delegate(a, b, c)
     f4 (17, 17)
     print '\t==== b, c'
     f4 -= a
     f4 (19, 19)
     print '\t==== c'
     f4 -= b
     f4 (21, 21)
     print '======== test delegate.__call__ return value'
     f3 = delegate(lambda x, y: x*y)
     assert f3(10, 11) == 10*11
     f3 = delegate(lambda x, y: x*y, lambda x, y: x**y)
     assert f3(10, 11) == 10**11
     print '======== test delegate.__call__ with empty exception (empty)'
     f4 = delegate (emptyExcept=True)
     try:
         f4 (3, 5)
     except RuntimeError, ex:
         print 'Exception:', ex
     print '======== test delegate.__call__ with empty exception (not empty)'
     f4 += a
     f4 (3, 5)
     print '======== test delegate.bind'
     print '\t==== a'
     f = delegate (a)
     f (911, 119)
     print '\t==== a, b'
     f.bind (b)
     f (199, 991)
     print '======== test delegate.unbind'
     print '\t==== b'
     f.unbind (a)
     f (177, 771)
     print '\t==== (empty)'
     f.unbind (b)
     f (133, 331)
     print '======== test delegate.clear'
     print '\t==== a, b'
     f = delegate (a, b)
     f (137, 138)
     print '\t==== (empty)'
     f.clear ()
     f (139, 139)
     print '======== (finished)'
'''
