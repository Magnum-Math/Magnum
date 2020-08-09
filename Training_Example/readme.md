## Training Examples
The directory contains the priming data for both the gpt instances 

### text2latex 
Contains subdirectories for source and target for the GPT model responsibe to convert RAW-TEXT from Wolfram to LaTEx 
if you wish to add or modify the priming data edit the corrosponding source and target text files. 
make sure that the respective soure and target pairs are on the same line in the text files

### text2Python
Contains subdirectories for source and target for the GPT model responsibe to convert RAW-TEXT from Wolfram to inline Python function used for graphing 
if you wish to add or modify the priming data edit the corrosponding source and target text files. 
make sure that the respective soure and target pairs are on the same line in the text files

### Testing_text
used for internal testing 


## A simple text to Latex priminng example (For Explanation)
**Note Each line is a priming example in itself** the current GPT3 model is limited to 2049 tokens, so the amout of priming data that can be provided is limited. It's recommended not to add redundant examples  

**Text**
```text
x^2 - 2 x - 6 = 0
Add 6 to both sides:
x^2 - 2 x = 6
Add 1 to both sides:
x^2 - 2 x + 1 = 7
Write the left hand side as a square:
(x - 1)^2 = 7
Take the square root of both sides:
x - 1 = sqrt(7) or x - 1 = -sqrt(7)
Add 1 to both sides:
x = 1 + sqrt(7) or x - 1 = -sqrt(7)
Add 1 to both sides:
Answer:  x = 1 + sqrt(7) or x = 1 - sqrt(7)
```
**Latex**
```latex
x^{2} - 2 x - 6 = 0
Add 6 \ to \ both \ sides:
x^{2} - 2 x = 6
Add 1 \ to \ both \ sides:
x^{2} - 2 x + 1 = 7
Write \ the \ left \ hand \ side \ as \ a \ square:
(x - 1)^{2} = 7
Take \ the \ square \ root \ of \ both \ sides:
x - 1 = \sqrt{7} \ or \ x - 1 = -\sqrt{7}
Add 1 \ to \ both \ sides:
x = 1 + \sqrt{7} \ or \ x - 1 = -\sqrt{7}
Add 1 \ to \ both \ sides:
Answer: x = 1 + \sqrt{7} \ or \ x = 1 - \sqrt{7}
```
