from plagiarismchecker.algorithm.ConsineSim import cosineSim ;
# from plagiarismchecker.algorithm import ConsineSim 
from apiclient.discovery import build

# searchEngine_API = 'AIzaSyAoEYif8sqEYvj1P6vYLw6CGMrQbDMmaq8'
# searchEngine_API = 'AIzaSyCUYy9AtdMUddiNA0gOcsGPQcE372ytyCw'
# searchEngine_API = 'AIzaSyAQYLRBBeDQNxADPQtUnApntz78-urWEZI'
searchEngine_API = 'AIzaSyCAeR7_6TTKzoJmSwmOuHZvKcVg_lhqvCc'
searchEngine_Id = '758ad3e78879f0e08'


# def cosineSim(text1, text2):
#     t1 = text1.lower()
#     t2 = text2.lower()
#     # print('t1 : ',t1, '\nt2 : ', t2)
#     vector1 = text_to_vector(t1)
#     vector2 = text_to_vector(t2)
#     cosine = get_cosine(vector1, vector2)
#     return cosine


def searchWeb(text, output, c):
    try:
        # Build Google Custom Search API request
        resource = build("customsearch", "v1", developerKey=searchEngine_API).cse()
        result = resource.list(q=text, cx=searchEngine_Id).execute()

        # Check if 'searchInformation' key exists
        if 'searchInformation' in result and int(result['searchInformation'].get('totalResults', 0)) > 0:
            maxSim = 0
            itemLink = ''

            # Ensure 'items' key exists in the result
            items = result.get('items', [])
            numList = min(len(items), 5)  # Get up to 5 search results

            for i in range(numList):
                item = items[i]
                content = item.get('snippet', '')  # Avoid missing key error
                simValue = cosineSim(text, content)

                if simValue > maxSim:
                    maxSim = simValue
                    itemLink = item.get('link', '')

                if item.get('link', '') in output:
                    itemLink = item['link']
                    break

            if itemLink:
                if itemLink in output:
                    output[itemLink] += 1
                    prev_count = output[itemLink] - 1
                    c[itemLink] = ((c[itemLink] * prev_count + maxSim) / output[itemLink]) if prev_count > 0 else maxSim
                else:
                    output[itemLink] = 1
                    c[itemLink] = maxSim
        else:
            print(f"No search results for: {text}")
            
    except Exception as e:
        print(f"Error searching for: {text}")
        print(e)
        return output, c, 1  # Indicate error

    return output, c, 0  # Indicate success


