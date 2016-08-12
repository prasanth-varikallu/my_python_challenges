import pickle

f = open('Banner.p', 'r')
result = pickle.load(f)
f.close

for li in result:
	print ''.join((l[0]*l[1] for l in li))
