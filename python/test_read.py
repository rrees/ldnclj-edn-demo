import edn_format
from sys import argv

if len(argv) < 1 + 1:
	print "Supply data file name"
	exit(1)

with open(argv[1], 'r') as f:
	data_string = f.read()
	print data_string

	data = edn_format.loads(data_string)
	print data

