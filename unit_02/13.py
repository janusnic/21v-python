#!/usr/bin/python

# 13.py in
def extract_from_tag(tag, line):
	opener = '<' + tag + '>'
	closer = '</' + tag + '>'
	try:
		i = line.index(opener)
		start = i + len(opener)
		j = line.index(closer, start)
		return line[start:j]
	except ValueError:
		return None



line = "<h2>interpreter the output</h2>"
tag = 'h2'

print(extract_from_tag(tag, line))

print(u'Hello\u0020World !')