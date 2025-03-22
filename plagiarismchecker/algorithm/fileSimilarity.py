import re
import math
from nltk.corpus import stopwords

	
def findFileSimilarity(inputQuery, database):
    universalSetOfUniqueWords = set()
    en_stops = set(stopwords.words('english'))

    # Convert to lowercase and split into words (removing punctuation)
    queryWordList = re.sub(r"[^\w\s]", " ", inputQuery.lower()).split()
    databaseWordList = re.sub(r"[^\w\s]", " ", database.lower()).split()

    # Filter out stopwords
    queryWordList = [word for word in queryWordList if word not in en_stops]
    databaseWordList = [word for word in databaseWordList if word not in en_stops]

    # Create a unique set of words from both documents
    universalSetOfUniqueWords.update(queryWordList)
    universalSetOfUniqueWords.update(databaseWordList)

    # If no words remain, return 0% similarity to avoid divide-by-zero error
    if not universalSetOfUniqueWords:
        return 0.0

    universalSetOfUniqueWords = list(universalSetOfUniqueWords)  # Convert to list

    # Term Frequency (TF) Vectors
    queryTF = [queryWordList.count(word) for word in universalSetOfUniqueWords]
    databaseTF = [databaseWordList.count(word) for word in universalSetOfUniqueWords]

    # Compute Dot Product
    dotProduct = sum(q * d for q, d in zip(queryTF, databaseTF))

    # Compute Magnitudes
    queryVectorMagnitude = math.sqrt(sum(q ** 2 for q in queryTF))
    databaseVectorMagnitude = math.sqrt(sum(d ** 2 for d in databaseTF))

    # Avoid division by zero
    if queryVectorMagnitude == 0 or databaseVectorMagnitude == 0:
        return 0.0

    # Compute Cosine Similarity Percentage
    matchPercentage =round( (dotProduct / (queryVectorMagnitude * databaseVectorMagnitude)) * 100 ,2 )
# 	print (universalSetOfUniqueWords)
# 	print()
# 	print (databaseWordList)


# 	print (queryTF)
# 	print (databaseTF)

    return matchPercentage

	
