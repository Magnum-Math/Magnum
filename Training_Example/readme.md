## Training Examples
The directory contains the priming data for both the GPT-3 instances.

### text2latex 
Contains subdirectories for source and target for the GPT-3 model responsibe to convert RAW-TEXT from Wolfram Alpha API to LaTeX .
If you wish to add or modify the priming data, edit the corresponding source and target text files. 
Make sure that the respective source and target pairs are on the same lines in the text files.

### text2Python
Contains subdirectories for source and target for the GPT-3 model responsibe to convert RAW-TEXT from Wolfram Alpha API to inline Python function used for Graphing. 
If you wish to add or modify the priming data, edit the corresponding source and target text files. 
Make sure that the respective source and target pairs are on the same lines in the text files.

### Testing_text
(Used for internal testing)


## A simple text to Latex priminng example (For Explanation)
**Note Each line is a priming example in itself** The current GPT3 model is limited to 2049 tokens, so the amount of priming data that can be provided is limited. It's recommended not to add redundant examples, If you have access to Fine-tuning API of OpenAI, then it is not a problem.  

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
