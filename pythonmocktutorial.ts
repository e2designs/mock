Script started on Tue Mar 22 15:58:14 2016
# python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mock import Mock
>>> my_mock = ( m Mock()
>>> my_mock.attribute
<Mock name='mock.attribute' id='140643362728272'>
>>> my_mock.method()
<Mock name='mock.method()' id='140643362761680'>
>>> from mock import MagicMock
>>> my_mock = MagicMock()
>>> my_mock['index']
<MagicMock name='mock.__getitem__()' id='140643335330832'>
>>> mock_attribute_1 = my_mock.attribute
>>> mock_attribute_2 = my_mock.attribute
>>> mock_attribute  _1 is mocke   _attribute  _2
True
>>> muy  y_mock.answer.return_value = 42
>>> my_mac  ock.ansser   wer()
42
>>> 
>>> mock_     my_mock.error.side_effect = ValueError('Error Message')
>>> mock_    y_mock.error()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 1062, in __call__
    return _mock_self._mock_call(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 1118, in _mock_call
    raise effect
ValueError: Error Message
>>> my_mock.get_next.side_effect = [1, 2, 3]
>>> moc y  y_mock.get_next()
1
>>> my_mock.get_next()
2
>>> my_mock.get_next()
3
>>> my_mock.get_next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 1062, in __call__
    return _mock_self._mock_call(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 1121, in _mock_call
    result = next(effect)
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 127, in next
    return _next(obj)
StopIteration
>>> my_mock.get_next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 1062, in __call__
    return _mock_self._mock_call(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 1121, in _mock_call
    result = next(effect)
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 127, in next
    return _next(obj)
StopIteration
>>> my) _mock.at  method()
<MagicMock name='mock.method()' id='140643335099024'>
>>> my_mock.method.called
True
>>> my_mock.method(1, 2, 3, a=4, b=5, c=6)
<MagicMock name='mock.method()' id='140643335099024'>
>>> my_mock.method( .assert_called_with(1.2.   , 2. / ,2  3, 4 a- =4, b=5, c=-5  56  6)
>>> my_mock.method.assert_called_with(1, 2, 3, a=4, b=5, c=6)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)[1P)')S)[1P)s)o)m)e);)')[1P)[1P)'),) )')o)t)h)e)r)'),) )')a)r)g)u)m)e)n)t)s)')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/mock/mock.py", line 937, in assert_called_with
    six.raise_from(AssertionError(_error_message(cause)), cause)
  File "/usr/local/lib/python2.7/dist-packages/six.py", line 718, in raise_from
    raise value
AssertionError: Expected call: method('some', 'other', 'arguments')
Actual call: method(1, 2, 3, a=4, b=5, c=6)
>>> exit()
# python t TestFacebook
python: can't open file 'TestFacebook': [Errno 2] No such file or directory
# ^[[A	^[[B^[[B            python tes   Test	Facebook.py
Traceback (most recent call last):
  File "TestFacebook.py", line 8, in <module>
    class SimpleFacebookTestCase(unittest.TestCase):
  File "TestFacebook.py", line 16, in SimpleFacebookTestCase
    mock_put_object.assert_called_with(message="Hello World!")
NameError: name 'mock_put_object' is not defined
# exit

Script done on Tue Mar 22 16:11:13 2016
