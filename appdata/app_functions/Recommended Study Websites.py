from colors_app import *
import webbrowser
import time


def Slow(text, delay=0.03):
    for line in text.split("\n"):
        print(line, flush=True)
        time.sleep(delay)


def MainColor2(text):
    start_color = (0, 200, 150)
    end_color = (0, 255, 255)

    num_steps = 16
    colors = [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1),
        )
        for i in range(num_steps)
    ]

    colors += list(reversed(colors[:-1]))

    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    result = []
    lines = text.split("\n")

    for i, line in enumerate(lines):
        color_index = i % len(colors)
        r, g, b = colors[color_index]
        colored_line = text_color(r, g, b) + line + "\033[0m"
        result.append(colored_line)

    return "\n".join(result)

# is that a minion studying?
#app banner
study = MainColor2(r"""                          
                                         ::::::::::::::::::::                                        
                                   ::::::::::::::::::::::::::::-:                                   
                               :::::::::::::::::::::::::::::::::::---                               
                            ::::::::::::::::::::::::::::::::::::::::---:                            
                          ::::::::::::::::::::::::::::::::::::::::::::----                          
                        :::::::::::::::::::::::::::::::::::::::::::::::::---                        
                      :::::---------::::::::::::::::::::::::::::---------:----                      
                     :::-=+**********+=-::::::::::::::::::::-=+**********+=----                     
                    ::=******************=::::::::::::::::=+*****************=--                    
                   :-+******        ******+-:::::---::::-+******        ******+--                   
                 ::-******            ******=+********+=*****+            ******=--                 
                 :-*****                ********************                *****=-                 
              *********                  *****=------=*****                  *********              
             **********      ++++++      ****+-::::::-+****      ++++++      **********             
               =-=+****     ++++++++     ****+-::::::-+****     ++++++++     *****===               
              --:-+****     ++++++++     ****+-::::::-+****     ++++++++     ****+----              
              -:::=*****    ++++++++    *****=::::::::=*****    ++++++++    *****=----              
              --::-+*****    ++++++    *****+-::::::::-+*****    ++++++    +****+-----              
             ---:::-+******          ******+-::::::::::-+******          ******+-------             
             ---:::::=********+  +********=::::::::::::::=********+  +********=-:------             
             ---:::::::=****************=::::::::::::::::::=****************=::::------             
             ---:::::::::-=++******++=-::::::::::::::::::::::-=++******++=-::::::------             
         ....:---:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::------:....         
         ......::::::::::::::::::::::::::-++++++++++++++++-:::::::::::::::::::::----:......         
        ...........:::::::::::::::::::::::=**************=:::::::::::::::::::::::...........        
    === ...............:::::::::::::::::::-=************+-:::::::::::::::::::............... ===    
    ======--:..............:::::::::::::::::-+********+-:::::::::::::::::..............:--======    
    =============::.............:::::::::::::::--==--:::::::::::::::.............::=============    
     =================-:::.........::::::::::::::::::::::::::::::.........:::-=================     
     =======================--:........::::::::::::::::::::::........:--=======================     
     =============================--:......::::::::::::::......:--=============================     
      ==================================-::.....:::::....::-==================================      
      ========================================--++++--=======================================-:     
     ::::::::-================================++++++++==================================-::::::--   
    -::::::::::-==============================++++++++================================-::::::::---  
    --::::::::::-=============================++++++++===============================-:::::::::---  
    ---::::::::::-============================++++++++==============================-:::::::::----  
     ---::::::::::-===========================++++++++=============================-:::::::::----   
     ----:::::::::-===========================++++++++=============================:::::::::----    
      ----::::-----===========================++++++++============================-:::::::::----    
       -----------============================++++++++=============================--:::::-----     
        --------==============================++++++++===============================---------      
           ===================================++++++++===================================           
           ===================================++++++++===================================           
            ==================================++++++++==================================            
             =================================++++++++=================================             
                  ============================++++++++============================                  
                      ========================++++++++========================                      
                           ===================++++++++===================                           
                                 =============++++++++=============                                 
                                     =========++++++++=========                                     
                                          ====++++++++====                                          
                                              ++++++++                                              
                                               ++++++                                               
                                                                                                         
""")
#list of websites
STUDY_WEBSITES = {
    "Khan Academy": "https://www.khanacademy.org",
    "Physics Classroom": "https://www.physicsclassroom.com",
    "Grammarly": "https://www.grammarly.com",
    "Wolfram Alpha": "https://www.wolframalpha.com",
    "Coursera": "https://www.coursera.org",
    "edX": "https://www.edx.org",
    "Quizlet": "https://quizlet.com",
    "Chegg": "https://www.chegg.com",
    "Study.com": "https://www.study.com",
    "BBC Bitesize": "https://www.bbc.co.uk/bitesize",
    "SparkNotes": "https://www.sparknotes.com",
    "MIT OpenCourseWare": "https://ocw.mit.edu",
    "Udemy": "https://www.udemy.com",
    "FutureLearn": "https://www.futurelearn.com",
    "Academia": "https://www.academia.edu",
    "OpenStax": "https://openstax.org",
    "W3Schools": "https://www.w3schools.com",
    "Duolingo": "https://www.duolingo.com",
    "Crash Course": "https://www.youtube.com/user/crashcourse",
    "TED-Ed": "https://ed.ted.com",
    "Google Scholar": "https://scholar.google.com",
    "BioMan Biology": "https://biomanbio.com",
    "TED Talks": "https://www.ted.com/talks",
    "Library Genesis": "https://libgen.is",
    "Art of Problem Solving": "https://artofproblemsolving.com",
    "Open Culture": "https://www.openculture.com",
    "YouTube EDU": "https://www.youtube.com/education",
    "Codeacademy": "https://www.codecademy.com",
    "Skillshare": "https://www.skillshare.com",
    "LinkedIn Learning": "https://www.linkedin.com/learning",
    "Memrise": "https://www.memrise.com",
    "Academic Earth": "https://academicearth.org",
    "PhET Interactive Simulations": "https://phet.colorado.edu",
    "Project Euler": "https://projecteuler.net",
    "Github": "https://github.com/",
    "Chatgpt": "https://chatgpt.com/",
    "The Math Learning Center": "https://www.mathlearningcenter.org",
    "Socratic": "https://www.socratic.org",
}




def display():
 for name, url in STUDY_WEBSITES.items():
    Slow(f""
          f"\n{red}[{cyan}!{red}]{lc} {name}{white}:{green} {url} {purple}|")




def open():
  choice = input(f"\n{yellow}Enter website name to open (or press Enter to skip):{red} ")
  if choice in STUDY_WEBSITES:
    webbrowser.open(STUDY_WEBSITES[choice])

Slow(study)
Slow(f"\n{blue}Recommended Study Websites:")
display()
open()
