import math

def shift(list):

	if len(list) > 0:
		temp = list[0]

	for i in range(len(list) - 1):
			list[i] = list[i + 1]

	list[len(list) - 1] = temp


def findPlainText(key, cipherText):
	plainText = ""

	key *= math.ceil(len(cipherText)/len(key))

	for i in range(len(cipherText)):
		if ord(key[i]) - ord(cipherText[i]) <= 0:
			plainText += chr((ord(key[i]) - ord(cipherText[i])) *-1 + 65)
		else:
			plainText += chr(26 - (ord(key[i]) - ord(cipherText[i])) + 65)

	return plainText


def frequencyAnalysis(cipherText):	#Implemented for alphabet (A-Z) only
	
	#setup
	offsetText = cipherText
	levelCoincidences = []
	frequencies = []
	for i in range(len(cipherText)):
		levelCoincidences.append(0)

	#STEP 1: FIND THE LENGTH OF THE KEY

	#find which offsets line up with the ciphertext
	for i in range(len(levelCoincidences)):
		offsetText = "$" + offsetText
		for j in range(len(cipherText)):
			if (cipherText[j] == offsetText[j]):
				levelCoincidences[i]+= 1

	print("Coincidences:")
	print(levelCoincidences)

	#implement finding keyLength here

	#-------------------------------------------------
	keyLength = 5
	#-------------------------------------------------

	#STEP 2: FIND THE KEY

	#find the frequency of each letter for each key letter

	cipherTextSeperated = []

	#build keyLength arrays of each character encoded by the specific key character
	for i in range(keyLength):
		cipherTextSeperated.append("")

	#now form strings of the ciphertext based on the key length
	for i in range(len(cipherText)):
		if i == 0 or i % keyLength == 0:
			cipherTextSeperated[0] += cipherText[i]
		else:
			prevIndex = i - 1
			while prevIndex != 0 and prevIndex % keyLength != 0:
				prevIndex -= 1
			cipherTextSeperated[i - prevIndex] += cipherText[i]

	print("")
	print("Here are the seperated strings:")		
	print(cipherTextSeperated)

	#now find the frequencies

	#frequencies[keyLength][26] (for A-Z)
	frequencies = []

	for i in range(keyLength):
		frequencies.append([])
		for j in range(26):
			frequencies[i].append(0)

	#now we have keyLength arrays of 0
	for i in range(len(cipherTextSeperated)):
		for j in range(len(cipherTextSeperated[i])):
			frequencies[i][ord(cipherTextSeperated[i][j]) - 65] += 1

	print("")
	print("Number of characters of each type:")
	print(frequencies)

	#now get frequencies for the alphabet (in the english language) and hard code them in
	englishFrequencies = []
	englishFrequencies.append(8.167 * (1/100))  #A
	englishFrequencies.append(1.492 * (1/100))  #B
	englishFrequencies.append(2.782 * (1/100))  #C
	englishFrequencies.append(4.253 * (1/100))  #D
	englishFrequencies.append(12.702 * (1/100)) #E
	englishFrequencies.append(2.228 * (1/100))  #F
	englishFrequencies.append(2.015 * (1/100))  #G
	englishFrequencies.append(6.094 * (1/100))  #H
	englishFrequencies.append(6.966 * (1/100))  #I
	englishFrequencies.append(0.153 * (1/100))  #J
	englishFrequencies.append(0.772 * (1/100))  #K
	englishFrequencies.append(4.025 * (1/100))  #L
	englishFrequencies.append(2.406 * (1/100))  #M
	englishFrequencies.append(6.749 * (1/100))  #N
	englishFrequencies.append(7.507 * (1/100))  #O
	englishFrequencies.append(1.929 * (1/100))  #P
	englishFrequencies.append(0.095 * (1/100))  #Q
	englishFrequencies.append(5.987 * (1/100))  #R
	englishFrequencies.append(6.327 * (1/100))  #S
	englishFrequencies.append(9.056 * (1/100))  #T
	englishFrequencies.append(2.758 * (1/100))  #U
	englishFrequencies.append(0.978 * (1/100))  #V
	englishFrequencies.append(2.360 * (1/100))  #W
	englishFrequencies.append(0.150 * (1/100))  #X
	englishFrequencies.append(1.974 * (1/100))  #Y
	englishFrequencies.append(0.074 * (1/100))  #Z

	#find out which shift results in the largest sum
	sums = []

	for i in range(len(frequencies)):
		currentSum = 0
		sums.append([])
		for j in range(len(frequencies[i])):
			for k in range(len(frequencies[i])):
				currentSum += frequencies[i][k] * englishFrequencies[k]
			sums[i].append(currentSum)
			currentSum = 0
			shift(frequencies[i])

	print("")
	print("Sums:")
	print(sums)

	keys = ["", "", ""]

	#now find out which shift is most effective
	for i in range(len(sums)):
		keys[0] += chr(sums[i].index(max(sums[i])) + 65)
		sums[i][sums[i].index(max(sums[i]))] =  -1
		keys[1] += chr(sums[i].index(max(sums[i])) + 65)
		sums[i][sums[i].index(max(sums[i]))] =  -1
		keys[2] += chr(sums[i].index(max(sums[i])) + 65)

	#STEP 3: FIND THE PLAINTEXT

	plainText = findPlainText(keys[0], cipherText)

	print("")
	print("Key: " + keys[0] + " Plaintext: ")
	print(plainText)

# Enter the string to decode here - this one is used as an example.
# If the key is known, simply use the function findPlainText(key, cipherText) instead.
frequencyAnalysis("JJXNEKUEGUODHVQZYEGEUSSGFGPDNCNFHORKSPROXFBURYRMQNRFYQPRRXGRXFJTHTBQHFOTJYBUUIQGNISHTNKLRUKRVGBLXSYQIRFVAGJDNCNFHFRGIGURJKLRFASIGUGIEQVUNEIRHRRQFLFVARCJSSUODWRYLKLRZGTLVAKNEFEGKLREJZJSVILPGGUFTREGKISBXPINEYIEQVUJLNQHVIABVVVNGKUFLZKRRFBLGVRFYZRTOAKXBAYRRQGAIRVAMUMNYYKLRAGJXURZVGUAUCSTLHVGNZKDSERYFTUVYKMPNZVHGUKTSAGXFPFJKIIZNJVXBHIYWRAYZXVIKPSHZKIIYLNRHGBHIYFUZYICNTVPFJOKLLBAIJVAMVVFAUNEYYEFYUNJKSQBCRWJNBVCBHXYEAQOEXURMVRREGCHVEKTXVBTFJGUKTSZCUEIAGYRRQUUGIVGYRZRQGCSGBLDYFPACEERDGIAQOKYERUWGBHXJIOHZDINAZKLNGEFYUNJKSFVZZRSHXZEGVTXPLFZZPYVLPSHJGEXRQZFORRVCMFGKEMATZFXURYRQRCXFKENSDIMNVYSQJGMIQNNRRQNTUXURIYEAAKCWJVZTLRQGXEVASFVRTAEOZHYZGOHZKLVFZZQRVZNEFNHRGXTXFYAQZFEARCJEAAULRPRSVRGGNVRRJYNEFNRNELFNVEIVRPIQVZVHGBLZXGUKILLGNDWBSZYIZHYZGNAJEIJFHISHTNKXBLULLREKFRGUKJYORZYEJNBVFNAJSVBNJTEFGOEKNEULRQGNVKNYGOCNEULRQGNVGYBIBWDHGNORQGMSVPKRRQJKCPORYRCVAMRFVTNVPYBZFEYYOEXRYRZKRAZCMSRLFVZFKMIELCYIERGEHGBKMIELUEIRYYVSHGZYIERZYIFRIIIGVYKSONTXXURXFGXFZFKRGNVVTHEJEAQUWGBHXJIGUKSMTAKNWFGUICGBTZKUGOJXURYVRFNZZSANRKLRSZFJGUKEIJVSGVB")
