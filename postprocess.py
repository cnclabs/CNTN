from itertools import izip
from collections import defaultdict

def load_setting( setting ):
	setting = open( setting ).readlines()
	return [i.split(' = ')[1].strip() for i in setting]

settings = load_setting( 'setting.txt' )
testing = open( settings[1] ).readlines()
predicted = open( settings[13] ).readlines()


keywords = defaultdict(list)
non_key = defaultdict(list)


for t, p in izip(testing, predicted):
	if p.strip() == '1':
		_ = t.split('_')

		keywords[_[0]].append(_[1])
	else:
		_ = t.split('_')

		non_key[_[0]].append(_[1])

for key in keywords.iterkeys():
	print key
	for i in keywords[key]:
		print '\t{}'.format(i)
	
	for i in non_key[key]:
		print '\t\t{}'.format(i)

