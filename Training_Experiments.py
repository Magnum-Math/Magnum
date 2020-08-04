#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
openai.api_key = "sk-Qgz3rmm3AbTBIwPjA0voHN3llTPWlsBPsNc8fUAd"


# In[8]:


from app import apiWrapper
print("Enter Input Question")
qry = input()
print("Would you like to print intermediate code results? yes/no")
selection = input()
while selection not in ["yes", "no"]:
    selection = input()
    print("Would you like to print intermediate code results? yes/no")

apiWrapper.getUsrQues(qry)
RAW_TEXT, Query = apiWrapper.callApi()
print("Query Received is ", Query)
print("Solution Generated")


# In[9]:


if selection == "yes":
    for line in RAW_TEXT:
        print(line)


# In[10]:


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
gpt = GPT(engine="curie",
          temperature=0.3,
          max_tokens=300)


# reade file and convert it to source string and target string tuples
source_names = [item for item in sorted(glob("./Training_Example/sources/*"))]
target_names = [item for item in sorted(glob("./Training_Example/latex/*"))]


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
        """
        print("Source: ", s_RAW)
        print("Output: ", t_RAW)
        print("----")
        """

"""
# Define UI configuration
config = UIConfig(description="Text to Manim Class",
                  button_text="Convert",
                  placeholder="Type Raw Text here")

demo_web_app(gpt, config)
"""


# In[11]:


## Testing Script
"""
testFiles = [item for item in sorted(glob("./Training_Example/Test/2..txt"))]
for file in testFiles:
    test_RAW = read_file(file)
    response = []
    for line in test_RAW:
        print("Prompt: ", line)
        t = gpt.get_top_reply(line)
        print(t,end="----\n")
        response.append(t)
"""


# In[13]:


# Converting RAW_TEXT to Latex:
print("Fetching the intermediate LateX code from OpenAI GPT3 API")
response = []
for line in RAW_TEXT :
    t = gpt.get_top_reply(line)
    response.append(t)
print("Intermediate LateX generated")


# In[14]:


latex_code = []
for line in response:
    latex_code.append(line.split("\n")[0][7:] + "\n")


# In[15]:


if selection == "yes":
    for line in latex_code:
        print(line, end="")


# In[17]:


from app import latex2Manim
print("Converting Latex to Maxnim Code")
manim_code = latex2Manim.latex2Manim(latex_code)
if selection == "yes":
    print(manim_code)
print("Manim Code Generated")


# In[18]:


fptr =  open("solution.py", "w") 
fptr.write(manim_code)
fptr.close()
print("Manim Code saved at ./solution.py")


# In[26]:


import os
print("Starting to Animate")
retval = os.system('manim solution.py Solution -pl --media_dir "./Animations"')
if retval == 0:
    print("Animation Completed check ./Animations/video for output")
else:
    print("Animation Error Check Manim Logs!!")


# In[10]:


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


# In[11]:


"""for l in retval:
    print (l)"""


# In[ ]:




