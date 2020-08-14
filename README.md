# MAGNUM (AI Math Animator powered by GPT-3 and Wolfram Alpha)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
## Visualize Beautiful Math solutions 
![Manim Logo](https://img.techpowerup.org/200811/magnum-2-1.png)

Initial release date: 15 August 2020

Fork Credits: The [gpt3-sandbox project](https://github.com/shreyashankar/gpt3-sandbox) was taken as the starting point for this project. We would like Thank the authons of GPT-3-Sandbox for all their help. :)
## Description

The goal of this project is to create an Open Source toolkit that makes Math animations effortless. Either from a plain English query or from formatted LaTeX! NO PYTHON CODING NEEDED.

This project addresses the following issues:

1. Create an end to end package using Wolfram Alpha and GPT-3 to visualize Step-by-step Math soultions to user questions.
2. Create a standalone package which enables you to convert LaTeX into beautiful animations without any knowledge of Manim.

For full docs and detailed information, have a look at our website: https://magnum.shreenabh.com/ 

## Setup

First, clone or fork this repository. Then to set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: `python -m venv $ENV_NAME`
2. Activate the virtual environment: ` source $ENV_NAME/bin/activate` (for MacOS, Unix, or Linux users) or ` .\ENV_NAME\Scripts\activate` (for Windows users)
3. Install requirements: `pip install -r requirements.txt`
4. To add your OpenAI Secret Key: Open the file called `openai` in the `api_keys` folder and add your Seceret Key there `$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'sk-somerandomcharacters'` (excluding quotes). If you are unsure what your secret key is, navigate to the [API docs](https://beta.openai.com/developer-quickstart) and copy the token displayed next to the "secret" key type.
5. To add your Wolfram Alpha AppID: open the file called `appid` int the `api_keys` folder and add your AppID there `$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'ZHR$%D-GET$%ASBF$'` (excluding quotes).

(For detailed Setup information for the no code playground, check our website)


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
We have provided you with the basic priming data for the text to Manim GPT-3 model. 
The LaTeX conversion is slightly non standard as the text is interperetd in TeX so to introduct spacing we have to insert a " / ". Another way of doing this is by explicitly declaring text as \text{Your Text Here}.

If you wish to provide your own examples for priming you can edit the files in the "Training_Examples" directory. 

### A note if you are using Non-Standard LaTeX packages 
We use Manim to animate the solution from Wolfram. Follow the instructions at [manim github page](https://github.com/3b1b/manim) to get Manim up and running.

If your LaTeX code uses non-standard or additional packages you will need the manim source code and NOT the "pip" version .

Again the instructions to install the required version are given on [Manim github page](https://github.com/3b1b/manim) or you can follow [the Manim docs here](https://readthedocs.org/projects/manim/downloads/pdf/latest/)

For non standard LaTeX packages, follow [this amazing video](https://www.youtube.com/watch?v=VPYmZWTjHoU)

### Rendering options for manim 
Manim provides you with a full array of rendering options from setting aspect ratios to resoultion and framerate. 

Follow the [video here to get insight on all the options](https://www.youtube.com/watch?v=d_2V5mC2hx0)

## Contributions

We actively encourage people to contribute by adding their own examples or even adding functionalities to the modules. Please make a pull request if you would like to add something, or create an issue if you have a question. We will update the contributors list on a regular basis.

Please *do not* leave your secret key and/or AppID in plaintext in your pull request!

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://shreenabh.com"><img src="https://avatars3.githubusercontent.com/u/62369422?v=4" width="100px;" alt=""/><br /><sub><b>Shreenabh Agrawal</b></sub></a><br /><a href="https://github.com/Magnum-Math/Magnum/issues?q=author%3AShreenabh664" title="Bug reports">🐛</a> <a href="https://github.com/Magnum-Math/Magnum/commits?author=Shreenabh664" title="Code">💻</a> <a href="#content-Shreenabh664" title="Content">🖋</a> <a href="https://github.com/Magnum-Math/Magnum/commits?author=Shreenabh664" title="Documentation">📖</a> <a href="#design-Shreenabh664" title="Design">🎨</a> <a href="#projectManagement-Shreenabh664" title="Project Management">📆</a></td>
    <td align="center"><a href="https://mrselukar.github.io"><img src="https://avatars1.githubusercontent.com/u/35305019?v=4" width="100px;" alt=""/><br /><sub><b>Mayur Selukar</b></sub></a><br /><a href="https://github.com/Magnum-Math/Magnum/commits?author=mrselukar" title="Code">💻</a> <a href="https://github.com/Magnum-Math/Magnum/issues?q=author%3Amrselukar" title="Bug reports">🐛</a> <a href="https://github.com/Magnum-Math/Magnum/commits?author=mrselukar" title="Documentation">📖</a> </td>
    <td align="center"><a href="https://github.com/Nanu00"><img src="https://avatars3.githubusercontent.com/u/66585423?v=4" width="100px;" alt=""/><br /><sub><b>Shantanu Deshmukh</b></sub></a><br /><a href="https://github.com/Magnum-Math/Magnum/commits?author=Nanu00" title="Code">💻</a> <a href="https://github.com/Magnum-Math/Magnum/issues?q=author%3ANanu00" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://www.arvidhya.com"><img src="https://avatars3.githubusercontent.com/u/26987169?v=4" width="100px;" alt=""/><br /><sub><b>Kartik Kinge</b></sub></a><br /><a href="#ideas-kingekartik" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
