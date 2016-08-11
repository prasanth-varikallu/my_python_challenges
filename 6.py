import pickle

f = open('Banner.p', 'r')
result = pickle.load(f)
f.close

print len(result)
print result