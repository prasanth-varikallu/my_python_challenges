import urllib, re

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
base_number = '12345'
i = 0
while (i < 400):
	resp = urllib.urlopen(base_url + base_number)
	text = resp.read()
	if not (re.search(ur'and the next nothing is [0-9]+', text)):
		print text
	base_number = ''.join(re.findall(r'[0-9]', text))
	i += 1

