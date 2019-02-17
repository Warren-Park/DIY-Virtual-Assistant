import http.client, json, sys
def process(text,credential):
    """PROCESSES text using Microsoft Azure QnA Maker
    https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/quickstarts/get-answer-from-knowledge-base-python
    """

    host = credential[2]+".azurewebsites.net"
    endpoint_key = credential[0]
    route = "/qnamaker/knowledgebases/"+credential[1]+"/generateAnswer"
    question = "{'question': '"+text+"'}"
    headers = {
        'Authorization': 'EndpointKey ' + endpoint_key,
        'Content-Type': 'application/json'
    }
    conn = http.client.HTTPSConnection(host, port=443)
    conn.request("POST", route, question, headers)
    response = conn.getresponse()
    answer = response.read()
    try:
        ans = json.loads(answer)["answers"][0]["answer"]
        if ans=="No good match found in KB.":
            ans = "Sorry. I am learning how to answer that question."
        return ans
    except:
         print("Unexpected error:", sys.exc_info()[0])
         print("Unexpected error:", sys.exc_info()[1])
         raise IOError("Error occurred with the connection.")



