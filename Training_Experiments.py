#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
openai.api_key = "sk-8fuZdYFOxSDQDfi3nbwhGH3fOJzZFDiezVwvIPBc"


# In[2]:


from app import apiWrapper
print("Enter Input Question")
qry = input()
qry += " "
while qry.isspace():
    qry = input("Enter Input Question")

print("Would you like to print intermediate code results? yes/no")
selection = input()
while selection not in ["yes", "no"]:
    selection = input()
    print("Would you like to print intermediate code results? yes/no")

apiWrapper.getUsrQues(qry)
RAW_TEXT, Query = apiWrapper.callApi()
Query = Query.replace("|","")
print("Query Received is ", Query)
print("Solution Generated")


# In[3]:


if selection == "yes":
    for line in RAW_TEXT:
        print(line)


# In[4]:


import os
import sys
sys.path.append(os.getcwd())

from api import GPT, Example, UIConfig
from api import demo_web_app
from glob import glob
def read_file(path_to_file):
    retval = ""
    file = open(path_to_file)
    retval = file.readlines()
    file.close()
    #Make sure the new line character is not read it throws the model off     
    retval = [x.split("/n")[0][:-1] for x in retval]
    return retval


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.01,
          max_tokens=300)


# reade file and convert it to source string and target string tuples
source_names = [item for item in sorted(glob("./Training_Example/text2latex/sources/*"))]
target_names = [item for item in sorted(glob("./Training_Example/text2latex/latex/*"))]


# open each file in the Training_Example directory
for src_path, target_path in zip(source_names,target_names):
    
    # For each files read the RAW and corrosponding Latex Code
    src_RAW = read_file(src_path)
    target_RAW = read_file(target_path)
    
    # for each pair of RAW and latex prime the GPT model
    if len(src_RAW) != len(target_RAW):
        raise Exception("Source and Latex have mismached number of line {} {} in file {} and {}".format(str(len(src_RAW)), str(len(target_RAW)),src_path,target_path))

    for s_RAW, t_RAW in zip(src_RAW,target_RAW):
        gpt.add_example(Example(s_RAW,t_RAW))
        # Uncomment the following if you would like to see the priming examples
        #print("Source: ", s_RAW)
        #print("Output: ", t_RAW)
        #print("----")
        
print("")


# In[5]:


import os
import sys
sys.path.append(os.getcwd())

from api import GPT, Example, UIConfig
from api import demo_web_app
from glob import glob
def read_file(path_to_file):
    retval = ""
    file = open(path_to_file)
    retval = file.readlines()
    file.close()
    #Make sure the new line character is not read it throws the model off     
    retval = [x.split("/n")[0][:-1] for x in retval]
    return retval


# Construct GPT object and show some examples
gpt_py = GPT(engine="davinci",
          temperature=0.01,
          max_tokens=100)


# reade file and convert it to source string and target string tuples
source_names = [item for item in sorted(glob("./Training_Example/text2py/sources/*"))]
target_names = [item for item in sorted(glob("./Training_Example/text2py/python/*"))]


# open each file in the Training_Example directory
for src_path, target_path in zip(source_names,target_names):
    
    # For each files read the RAW and corrosponding Latex Code
    src_RAW = read_file(src_path)
    target_RAW = read_file(target_path)
    
    # for each pair of RAW and latex prime the GPT model
    if len(src_RAW) != len(target_RAW):
        raise Exception("Source and Latex have mismached number of line {} {} in file {} and {}".format(str(len(src_RAW)), str(len(target_RAW)),src_path,target_path))

    for s_RAW, t_RAW in zip(src_RAW,target_RAW):
        gpt_py.add_example(Example(s_RAW,t_RAW))
        # Uncomment the following if you would like to see the priming examples
        #print("Source: ", s_RAW)
        #print("Output: ", t_RAW)
        #print("----")
        
print("")


# In[13]:


# Converting RAW_TEXT Query to Python Function:
print("Attempting to convert input query to graphable python function")
python_func = gpt_py.get_top_reply(Query)
python_func = python_func[7:]
print("Interpereted python function is", python_func)


# In[17]:


# Converting RAW_TEXT to Latex:
from tqdm.auto import tqdm
print("Fetching the intermediate LateX code from OpenAI GPT3 API")
response = []
for i in tqdm(range(len(RAW_TEXT))) :
    line = RAW_TEXT[i]
    t = gpt.get_top_reply(line)
    response.append(t)
print("Intermediate LateX generated")


# In[18]:


latex_code = []
for line in response:
    text = line.split("\n")[0][7:]
    if text.isspace() or text == "":
        continue
    else:
        latex_code.append(text + "\n")


# In[19]:


if selection == "yes":
    for line in latex_code:
        print(line, end="")


# In[27]:


from app import latex2Manim
import importlib
importlib.reload(latex2Manim)
print("Converting Latex to Maxnim Code")
manim_code = latex2Manim.latex2Manim(latex_code,Query ,python_func)
if selection == "yes":
    print(manim_code)
print("Manim Code Generated")


# In[28]:


fptr =  open("solution.py", "w") 
fptr.write(manim_code)
fptr.close()
print("Manim Code saved at ./solution.py")


# In[29]:


#!manim solution.py Solution -pl --media_dir "./Animations"


# In[ ]:


import os
print("Starting to Animate")
retval = os.system('manim solution.py Solution -pl --media_dir "./Animations"')
if retval == 0:
    print("Animation Completed check ./Animations/video for output")
else:
    print("Animation Error Check Manim Logs!!")


# In[ ]:


"""
# Script to find and replace spaces with " / " in files 
target_names = [item for item in sorted(glob("./Training_Example/latex/*"))]
retval = ""
for path_to_file in target_names:
    print(path_to_file)
    temp = input()
    if temp == "yes":

        file = open(path_to_file)
        retval = file.readlines()
        file.close()
        for i in range(len(retval)):
            print(retval[i])
            x = input()
            if x != '0':
                retval[i] = retval[i].replace(" ", " \ ")
        retval = [x.split("/n")[0][:-1] for x in retval]
    #print(retval)

"""


# In[ ]:


"""for l in retval:
    print (l)"""


# In[ ]:


def func(x_in):
		f = lambda x : eval(x_in)
		return f


# In[ ]:


a = func('x**2')


# In[ ]:


[a(i) for i in range(5)]


# In[ ]:




