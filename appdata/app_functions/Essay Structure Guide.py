from colors_app import *
import webbrowser
import sys

print(f'''
{green}Select options below:
{lc}=========================================================================||
{purple}Current options for Essay guide:                                     
{cyan}[{white}1{cyan}]{yellow} Website {green} (matrix) 
{cyan}[{white}2{cyan}]{yellow} Basic guide 
{cyan}[{white}3{cyan}]{red} Exit app                                      
{lc}=========================================================================||
''')

x = input(f'{yellow}Enter option {blue}(1,2,3):{red} ')

def web():
    webbrowser.open('https://www.matrix.edu.au/essay-writing-guide/overview/')

def base():
    print(f"""\n{lc}Essay Structure Guide:
    {green}1. Introduction:{white}
     {lc}  -{white} Hook/Attention Grabber
     {lc}  -{white} Background Information
      {lc} -{white} Thesis Statement

   {green} 2. Body Paragraphs: {white}
      {lc} - {white}Topic Sentence
     {lc}  -{white} Evidence & Explanation
      {lc} - {white}Link to Thesis

  {green}  3. Conclusion: {white}
     {lc}  -{white} Restate Thesis
      {lc} -{white} Summarize Key Points
      {lc} -{white} Closing Thought
    """)


if x in ['1', 'one', 'first']:
    web()
elif x in ['2', 'two', 'second']:
    base()
elif x in ['3', 'three', 'ThREE', 'exit']:
    sys.exit()
else:
    print(f'{red}INVALID!')