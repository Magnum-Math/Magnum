import app.apiInterface as api, untangle

# Makes an apiInput object from the apiInterface module
# Reads the appid file to get appid for the api
apiWrap = api.apiInput(open('./app/appid').readline().rstrip('\n'))

rques = ''
ques = 'NO INPUT'

def getUsrQues(inStr, textBool = True, stepBool = True):

    # For our application we need plaintext and steps parameters, so this function handles only them

    # Another function CAN be made that could handle more parameters, but it is not needed here

    global rques

    # One line conditionals to add parameters
    apiWrap.add2params('input', inStr)
    apiWrap.add2params('podstate', 'Step-by-step solution') if textBool else apiWrap.add2params('podstate', '')
    apiWrap.add2params('format', 'plaintext') if textBool else apiWrap.add2params('format', '')

    rques = inStr

    return None


def callApi():

    # Function to send the queries and parameters to the api

    theorem = False
    graph = False

    global ques

    result = apiWrap.getResult()    # result is an xml file
    answer = {}     # Variable that stores the parsed xml object

    for pod in result.queryresult.pod:

        # Tries to find all the relevant data from the xml object

        for spod in pod.subpod:
            # Makes a dictionary out of all the plaintext cdata
            try:
                answer[(pod['id'], spod['title'])] = str(spod.plaintext.cdata)
 #               print(spod.plaintext.cdata)
#                print(answer[(pod['id'], spod['title'])])
            except:
                print('No text in ' + pod['id'] + spod['title'])
                pass

    steps = ''      # To store steps

    for element in answer.keys():
        # Finds the steps and the input as interpreted by the api)
        if 'Possible intermediate steps' in element and element == 'Input':
            steps = answer[element]
        if element[0] == 'Input' and element[1] == '':
            ques = str(answer[element])
        if 'history' in element[0].lower()+element[1].lower():
            theorem = True

    if 'graph' in rques.lower() or 'plot' in rques.lower():
        graph = True

    if ques == 'NO INPUT':      #Gets the user input if nothing is returned by walpha
        ques = rques

    if theorem or graph:     #If the input asks for a theorem/formula/graph then all plaintext is returned
        steps = steps.join([i + "\n" for i in answer.values()])

    if steps == '':         #If no steps returned and the input isn't a theorem/formula, the pod with max chars is returned
        for element in answer.keys():
            if len(steps) < len(answer[element]):
                steps = answer[element]


    steps = steps.split('\n')       #These lines fix the answer's last newline problem by joining last two lines

    if len(steps) > 2:
        steps[-2] += steps[-1]
        steps.pop()

    steps = ''.join([i + '\n' for i in steps])

    steps = steps.replace('| ', '').split('\n')


#    return (answer, steps, ques)   #Uncomment if you want the complete parsed xml file (returned in the answer variable)

    return (steps, ques)
    #ques is interpreted input, if returned by the api. Otherwise it is the user's input