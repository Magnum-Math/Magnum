# AI MATH Animator powered by GPT-3 and Wolfram Alpha
## Visualize Math solutions 

Initial release date: 8 Aug 2020

Fork Credits: The [gpt3-sandbox project](https://github.com/shreyashankar/gpt3-sandbox) was taken as the starting point for this project. We would like thank the authons of gp3-sandbox for all there help :)
## Description

The goal of this project is to enable users to create cool web demos using the newly released OpenAI GPT-3 API **with just a few lines of Python.** 

This project addresses the following issues:

1. Goal1 
2. Goal2
Here is a simple example 
Note that this repository is currently not intended for production use and has limited capabelities .

## Background

GPT-3 ([Brown et al.](https://arxiv.org/abs/2005.14165)) is OpenAI's latest language model. It incrementally builds on model architectures designed in [previous](https://arxiv.org/abs/1706.03762) [research](https://arxiv.org/abs/1810.04805) studies, but its key advance is that it's extremely good at "few-shot" learning. There's a [lot](https://twitter.com/sharifshameem/status/1282676454690451457) [it](https://twitter.com/jsngr/status/1284511080715362304?s=20) [can](https://twitter.com/paraschopra/status/1284801028676653060?s=20) [do](https://www.gwern.net/GPT-3), but one of the biggest pain points is in "priming," or seeding, the model with some inputs such that the model can intelligently create new outputs. Many people have ideas for GPT-3 but struggle to make them work, since priming is a new paradigm of machine learning. Additionally, it takes a nontrivial amount of web development to spin up a demo to showcase a cool idea. We built this project to make our own idea generation easier to experiment with.

This [developer toolkit](https://www.notion.so/API-Developer-Toolkit-49595ed6ffcd413e93ebff10d7e70fe7) has some great resources for those experimenting with the API, including sample prompts.

## Requirements

Coding-wise, you only need Python. But for the app to run, you will need:

* API key from the OpenAI API beta invite
* Python 3
* Wolfram Alpha API-Key

Instructions to install Python 3 are [here](https://realpython.com/installing-python/)
Rest of the requirments are in requirements.txt and can be installed with 
'''python
pip3 install -r requirements.txt
'''

## Setup

First, clone or fork this repository. Then to set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: `python -m venv $ENV_NAME`
2. Activate the virtual environment: ` source $ENV_NAME/bin/activate` (for MacOS, Unix, or Linux users) or ` .\ENV_NAME\Scripts\activate` (for Windows users)
3. Install requirements: `pip install -r requirements.txt`
4. To add your secret key: create a file anywhere on your computer called `openai.cfg` with the contents `OPENAI_KEY=$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'sk-somerandomcharacters'` (including quotes). If you are unsure what your secret key is, navigate to the [API docs](https://beta.openai.com/developer-quickstart) and copy the token displayed next to the "secret" key type.


## Interactive Priming

The real power of GPT-3 is in its ability to learn to specialize to tasks given a few examples. However, priming can at times be more of an art than a science. Using the GPT and Example classes, you can easily experiment with different priming examples and immediately see their GPT on GPT-3's performance. Below is an example showing it improve incrementally at translating English to LaTeX as we feed it more examples in the python interpreter: 

```
>>> from api import GPT, Example, set_openai_key
>>> gpt = GPT()
>>> set_openai_key(key)
>>> prompt = "integral from a to b of f of x"
>>> print(gpt.get_top_reply(prompt))
output: integral from at to be of f of x

>>> gpt.add_example(Example("Two plus two equals four", "2 + 2 = 4"))
>>> print(gpt.get_top_reply(prompt))
output:

>>> gpt.add_example(Example('The integral from zero to infinity', '\\int_0^{\\infty}'))
>>> print(gpt.get_top_reply(prompt))
output: \int_a^b f(x) dx

``` 

## Contributions

We actively encourage people to contribute by adding their own examples or even adding functionalities to the modules. Please make a pull request if you would like to add something, or create an issue if you have a question. We will update the contributors list on a regular basis.

Please *do not* leave your secret key in plaintext in your pull request!

## Authors

The following authors have committed 20 lines or more (ordered according to the Github contributors page):

* (Mayur Selukar)[https://www.linkedin.com/in/mayur-selukar/]
* Shantanu Deshmukh
* Shreenabh Agrawal
* (The gpt3-sandbox team)[https://github.com/shreyashankar/gpt3-sandbox]
 


