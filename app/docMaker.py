# DO NOT USE THIS FOR API INTEGRATION
# FOR DEBUGGING ONLY

import apiWrapper as api
import pickle

ques = input('Question?>')
api.getUsrQues(ques)

result = api.callApi()

print('\n\n')
print('Input:' + result[1])
print('Steps:' + str(result[0]))
print('\n\n')

'''test = open('testQueries.txt', 'a')

test.write('\n\n######################\nQuestion == ' + ques + '\n######################\n\n')

for item in result[0]:
    line = str(item[0]) + ', ' + str(item[1]) + ' :=: \n' + str(result[0][item]) + '\n\n'
    #print(line)
    test.write(line)    
    
test.write('\n\n######################\n')
test.close()

querList = []

pickletest = open('testQueries', 'rb')
try:
    querList = pickle.load(pickletest)
    querList.append(result)
    #print(querList)
except:
    pass
pickletest.close()
pickletest = open('testQueries', 'wb')
pickle.dump(querList, pickletest)
pickletest.close()

#print(api.apiWrap.callURL)'''