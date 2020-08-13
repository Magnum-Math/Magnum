# MAGNUM (AI Math Animator powered by GPT-3 and Wolfram Alpha)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
## Visualize Beautiful Math solutions 

Initial release date: 8 Aug 2020

Fork Credits: The [gpt3-sandbox project](https://github.com/shreyashankar/gpt3-sandbox) was taken as the starting point for this project. We would like thank the authons of gp3-sandbox for all there help :)
## Description

The goal of this project is to enable users to create cool web demos using the newly released OpenAI GPT-3 API **with just a few lines of Python.** 

This project addresses the following issues:

1. Create an end to end package using wolfram and GPT3 to visualize math soultions to user questions.
2. Create a standaone package which enables you to convert latex into beautiful animations without any knowledge of manim.
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
Rest of the requirments are in requirements.txt

## Setup

First, clone or fork this repository. Then to set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: `python -m venv $ENV_NAME`
2. Activate the virtual environment: ` source $ENV_NAME/bin/activate` (for MacOS, Unix, or Linux users) or ` .\ENV_NAME\Scripts\activate` (for Windows users)
3. Install requirements: `pip install -r requirements.txt`
4. To add your openai secret key: open the file called `openai` int the `api_keys` folder and add your seceret key there `$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'sk-somerandomcharacters'` (excluding quotes). If you are unsure what your secret key is, navigate to the [API docs](https://beta.openai.com/developer-quickstart) and copy the token displayed next to the "secret" key type.
5. To add your wolfram alpha secret key: open the file called `appid` int the `api_keys` folder and add your seceret key there `$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'ZHR$%D-GET$%ASBF$'` (excluding quotes).


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
### Using Custom Priming Data
We have provided you with the basic priming data for the text to manim GPT model. 
The Latex conversion is slightly non standard as the text is interperetd in tex so to introduct spacing we have to inserte a " / ". 

If you wish to provide your own examples for priming you can edit the files in the Training_Examples directoriy. 

### A note if you are using non standard latex packages 
We use Manim to animate the solution from wolfram follow the instructions at [manim github page](https://github.com/3b1b/manim) to get manim up and running 

If your latex code uses non-standard or additional packages you will need the manim source code and not the pip version 

Again the instructions to install the required version are given on [manim github page](https://github.com/3b1b/manim) or you can follow [the manim docs here](https://readthedocs.org/projects/manim/downloads/pdf/latest/)

For non standard latex packages follow [this amazing video](https://www.youtube.com/watch?v=VPYmZWTjHoU)

### Rendering options for manim 
Manim provides you with a full array of rendering options from setting aspect ratios to resoultion and framerate. 

Follow the [video here to get insight on all the options](https://www.youtube.com/watch?v=d_2V5mC2hx0)

## Contributions

We actively encourage people to contribute by adding their own examples or even adding functionalities to the modules. Please make a pull request if you would like to add something, or create an issue if you have a question. We will update the contributors list on a regular basis.

Please *do not* leave your secret key and/or appif in plaintext in your pull request!

## Authors

The following authors have committed 20 lines or more (ordered according to the Github contributors page):

* [Mayur Selukar](https://www.linkedin.com/in/mayur-selukar/)
* Shantanu Deshmukh
* Shreenabh Agrawal
* [The gpt3-sandbox team](https://github.com/shreyashankar/gpt3-sandbox)
 



## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://shreenabh.com"><img src="https://avatars3.githubusercontent.com/u/62369422?v=4" width="100px;" alt=""/><br /><sub><b>Shreenabh Agrawal</b></sub></a><br /><a href="https://github.com/Magnum-Math/Magnum/issues?q=author%3AShreenabh664" title="Bug reports">🐛</a> <a href="https://github.com/Magnum-Math/Magnum/commits?author=Shreenabh664" title="Code">💻</a> <a href="#content-Shreenabh664" title="Content">🖋</a> <a href="https://github.com/Magnum-Math/Magnum/commits?author=Shreenabh664" title="Documentation">📖</a> <a href="#design-Shreenabh664" title="Design">🎨</a> <a href="#projectManagement-Shreenabh664" title="Project Management">📆</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!