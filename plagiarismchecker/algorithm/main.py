
from nltk.corpus import stopwords
from plagiarismchecker.algorithm import webSearch
import sys
import re
import math 

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).
def getQueries(text, n):
    sentenceEnders = re.compile(r'[.!?]\s*')
    sentenceList = sentenceEnders.split(text)
    
    sentencesplits = []
    en_stops = set(stopwords.words('english'))

    for sentence in sentenceList:
        words = re.findall(r'\b\w+\b', sentence)
        filtered_words = [word for word in words if word.lower() not in en_stops]
        
        if filtered_words:
            sentencesplits.append(filtered_words)

    finalq = []
    for sentence in sentencesplits:
        l = len(sentence)

        if l >= n:  # Generate n-grams
            for i in range(l - n + 1):
                finalq.append(sentence[i:i + n])
        else:
            if l > 1:  # ✅ Fixed condition
                finalq.append(sentence)

    print("Final Extracted Queries:", finalq)
    return finalq

def findSimilarity(text):
    # n-grams N VALUE SET HERE
    n = 9
    print("Queries before processing:", text)
    queries = getQueries(text, n)
    print('GetQueries task complete' , queries)
    print("Queries:", queries)
    q = [' '.join(d) for d in queries]
    output = {}
    c = {}
    i = 1
    while("" in q):
        q.remove("")
    count = len(q)
    if count > 100:
        count = 100
    numqueries = count
    for s in q[0:count]:
        output, c, errorCount = webSearch.searchWeb(s, output, c)
        print('Web search task complete')
        numqueries = numqueries - errorCount
        # print(output,c)
        sys.stdout.flush()
        i = i+1
    totalPercent = 0
    outputLink = {}
    print(output, c)
    prevlink = ''
    for link in output:
        percentage = (output[link] * c[link] * 100) / numqueries
        percentage = round(percentage, 2)  # Prevent floating-point errors

        print(f"Link: {link}, Percentage: {percentage}, Total Before: {totalPercent}")

        if percentage > 10:
            totalPercent += percentage
            prevlink = link
            outputLink[link] = percentage
        elif prevlink and prevlink in outputLink:
            totalPercent += percentage
            outputLink[prevlink] += percentage
        elif c[link] == 1:
            totalPercent += percentage

    print(f"Total After: {totalPercent}")
    totalPercent = math.ceil(totalPercent * 100) / 100
    print(count, numqueries)
    print(totalPercent, outputLink)
    print("\nDone!")
    return totalPercent, outputLink
