from random import randint, seed, choice, random
import string
import sys
import itertools

def generate_random_docs(n_docs, max_doc_length):
	docs = []
	seed(5)
	for i in range(n_docs):
		docs.append(''.join(choice('aaeioutgrb ') for _ in range(randint(int(max_doc_length*.75), max_doc_length))))

	for i in range(10):
		permuted_doc = list(choice(docs))
		permuted_doc[randint(0,len(permuted_doc))] = choice('1234567890')
		docs.append(''.join(permuted_doc))

	return docs

def generate_shingles(doc, shingle_size):
	shingles = set([])
	for i in range(len(doc)-shingle_size+1):
		shingles.add(doc[i:i+shingle_size])
	return shingles

def get_minhash(shingles, n_hashes):
	seed(0)
	minhash_row = []
	for i in range(n_hashes):
		randomStr = str(random())
		minhash = sys.maxint
		for shingle in shingles:
			hash_candidate = abs(hash(shingle + randomStr))
			if hash_candidate < minhash:
				minhash = hash_candidate
		minhash_row.append(minhash)
	return minhash_row

def get_band_hashes(minhash_row, band_size):
	band_hashes = []
	for i in range(len(minhash_row)):
		if i % band_size == 0:						
			if i > 0:
				band_hashes.append(band_hash)
			band_hash = 0
		band_hash += hash(minhash_row[i])		
	return band_hashes

def get_similar_docs(docs, n_hashes=400, band_size=7, shingle_size=3):
	hash_bands = {}
	for doc in docs:
		shingles = generate_shingles(doc, shingle_size)
		minhash_row = get_minhash(shingles, n_hashes)
		band_hashes = get_band_hashes(minhash_row, band_size)
		
		for i in range(len(band_hashes)):
			if i not in hash_bands:
				hash_bands[i] = {}
			if band_hashes[i] not in hash_bands[i]:
				hash_bands[i][band_hashes[i]] = [doc]
			else:
				hash_bands[i][band_hashes[i]].append(doc)

	similar_docs = set()
	for i in hash_bands:
		for hash_num in hash_bands[i]:
			if len(hash_bands[i][hash_num]) > 1:
				for pair in itertools.combinations(hash_bands[i][hash_num], r=2):
					similar_docs.add(pair) 

	return similar_docs
		
if __name__ == '__main__':
	n_hashes = 200
	band_size = 7
	shingle_size = 3
	n_docs = 1000
	max_doc_length = 20

	docs = generate_random_docs(n_docs, max_doc_length)

	similar_docs = get_similar_docs(docs, n_hashes, band_size, shingle_size)

	print similar_docs
	r = float(n_hashes/band_size)
	similarity = (1/r)**(1/float(band_size))
	print "similarity: %f" % similarity
	print "# Similar Pairs: %d" % len(similar_docs)