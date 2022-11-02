name_bytes = b'r\xc3\xa9sum\xc3\xa9'
name_str = name_bytes.decode()
print('UTF-8', name_str)
name_latin1 = name_str.encode('Latin1')
name_str = name_latin1.decode('Latin1')
print('Latin1', name_str)
