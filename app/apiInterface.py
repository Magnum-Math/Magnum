import urllib.parse, urllib.request, untangle
# Uses the untangle lib to make the walpha api's xml output into a python object

class apiInput:
    
    parsedURL = {       # Dictionary used to construct the final URL
            'scheme'  : 'http',
            'netloc'  : 'api.wolframalpha.com',
            'path'    : '/v2/query',
            'params'  : '',
            'query'   : '',
            'fragment': ''
            }
    callURL = ''        #Final URL variable, print this to see the xml file for debugging
    params = {}         #Parameters to be passed to the api

    def __init__(self, api_key):
        self.params['appid'] = api_key  # Gets the api key
    
#    def getInput(self, instr):
#        self.params['input'] = [instr]

    def add2params(self, paramName, paramStr):
        self.params[paramName] = [paramStr]

    def getResult(self):

        #The next 4 lines construct the URL
        self.parsedURL['query'] = urllib.parse.urlencode(self.params, doseq=True)
        self.callURL = urllib.parse.urlunparse(self.parsedURL.values())
        

        #Sending the URL to the api
        self.result = urllib.request.urlopen(self.callURL)
        self.parsedResult = untangle.parse(self.result)

        return self.parsedResult    # returns the xml file
