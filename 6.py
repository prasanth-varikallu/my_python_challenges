import pickle

f = open('Banner.p', 'r')
result = pickle.load(f)
f.close

for li in result:
	print li