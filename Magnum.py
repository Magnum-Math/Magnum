#!/usr/bin/env python
# coding: utf-8

# ## Convert your Math Question to Animated solution
# This is the main notebook for the Magnum Project 
# The installation instructions for all the dependencies are in the readme at our [github repository](https://github.com/GPT-3-Manim/AI-Math-Animator-GPT3) 
# 
# ### Using Custom Priming Data
# We have provided you with the basic priming data for the text to manim GPT model. 
# The Latex conversion is slightly non standard as the text is interperetd in tex so to introduct spacing we have to inserte a " / ". 
# 
# If you wish to provide your own examples for priming you can edit the files in the Training_Examples directoriy. 
# 
# ### A note if you are using non standard latex packages 
# We use Manim to animate the solution from wolfram follow the instructions at [manim github page](https://github.com/3b1b/manim) to get manim up and running 
# 
# If your latex code uses non-standard or additional packages you will need the manim source code and not the pip version 
# 
# Again the instructions to install the required version are given on [manim github page](https://github.com/3b1b/manim) or you can follow [the manim docs here](https://readthedocs.org/projects/manim/downloads/pdf/latest/)
# 
# For non standard latex packages follow [this amazing video](https://www.youtube.com/watch?v=VPYmZWTjHoU)
# 
# ### Rendering options 
# Manim provides you with a full array of rendering options from setting aspect ratios to resoultion and framerate. 
# 
# Follow the [video here to get insight on all the options](https://www.youtube.com/watch?v=d_2V5mC2hx0)

# In[1]:


import openai
import os 
from pathlib import Path
data_folder = Path(os.getcwd())
openai.api_key = open(data_folder / 'api_keys/openai').readline().rstrip('\n')
print(data_folder)


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

from api import GPT, Example
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
          max_tokens=150)


# reade file and convert it to source string and target string tuples
source_names = [item for item in sorted(glob(str(data_folder / "Training_Example/text2latex/sources/*")))]
target_names = [item for item in sorted(glob( str(data_folder / "Training_Example/text2latex/latex/*")))]


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
        


# In[5]:


# Construct GPT object and show some examples
gpt_py = GPT(engine="davinci",
          temperature=0.01,
          max_tokens=100)


# reade file and convert it to source string and target string tuples
source_names = [item for item in sorted(glob( str(data_folder / "Training_Example/text2py/sources/*")))]
target_names = [item for item in sorted(glob( str(data_folder / "Training_Example/text2py/python/*")))]


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


# In[6]:


# Converting RAW_TEXT Query to Python Function:
print("Attempting to convert input query to graphable python function")
python_func = gpt_py.get_top_reply(Query)
python_func = python_func[7:]
python_func = python_func.split("/n")[0]
print("Interpereted python function is", python_func)


# In[7]:


# Converting RAW_TEXT to Latex:
from tqdm.auto import tqdm
print("Fetching the intermediate LateX code from OpenAI GPT3 API")
response = []
for i in tqdm(range(len(RAW_TEXT))) :
    line = RAW_TEXT[i]
    t = gpt.get_top_reply(line)
    response.append(t)
print("Intermediate LateX generated")


# In[8]:


latex_code = []
for line in response:
    text = line.split("\n")[0][7:]
    if text.isspace() or text == "":
        continue
    else:
        latex_code.append(text +"\n")


# In[9]:


f = open('./latex.txt','w')
for i in range(len(latex_code)):
    f.write(latex_code[i])
f.close()


# In[10]:


if selection == "yes":
    for line in latex_code:
        print(line, end="")
    


# In[11]:


python_func = python_func.split("\n")[0]


# In[12]:


from app import latex2Manim
import importlib
importlib.reload(latex2Manim)
print("Converting Latex to Maxnim Code")
manim_code = latex2Manim.latex2Manim(latex_code, python_func ,python_func)
if selection == "yes":
    print(manim_code)
print("Manim Code Generated")


# In[13]:


fptr =  open(data_folder / "solution.py", "w") 
fptr.write(manim_code)
fptr.close()
print("Manim Code saved at {}/solution.py".format(data_folder))


# In[16]:


# if you are rendering inside the notebook use the cell below
#get_ipython().system('manim solution.py Solution -pl --media_dir "./Animations"')


# In[15]:


# code to make the magnum.py file

import os
print("Starting to Animate. Arguments for manim if any?")
args = input()
retval = os.system('manim ' + str(data_folder) + '/solution.py Solution ' + args +' --media_dir ' + str(data_folder) +'"/Animations"')
if retval == 0:
    print("Animation Completed check ./Animations/video for output")
else:
    print("Animation Error Check Manim Logs!!")


