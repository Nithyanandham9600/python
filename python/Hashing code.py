from collections import defaultdict

def groupAnagrams(words):
	hashmap = defaultdict(list)
	for word in words:
		key = ''.join(sorted(word))
		hashmap[key].append(word)
	return list(hashmap.values())

words = ["dusty", "study", "race", "care", "acre", "heart", "earth"]
groups = groupAnagrams(words)

for group in groups:
	print(group)