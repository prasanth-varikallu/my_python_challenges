import urllib, re

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
base_number = '12345'
i = 0
while (i < 100):
	resp = urllib.urlopen(base_url + base_number)
	text = resp.read()
	base_number = ''.join(re.findall(r'[0-9]', text))
	i += 1
	print i, base_number

print base_number, i

