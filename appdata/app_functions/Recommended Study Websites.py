from colors_app import *
import time 

#animation
def Slow(text, delay=0.03):
    for line in text.split("\n"):
        print(line, flush=True)
        time.sleep(delay)

#colours for banner
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
'''
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
'''
# dictionary of links
try:
    links = {
        "Physics": {
            "Khan Academy": "https://www.khanacademy.org/science/physics",
            "HyperPhysics": "http://hyperphysics.phy-astr.gsu.edu/",
            "Physics Classroom": "https://www.physicsclassroom.com/",
            "MIT OpenCourseWare": "https://ocw.mit.edu/courses/physics/",
            "PhET Interactive Simulations": "https://phet.colorado.edu/"
        },
        "Mathematics": {
            "Khan Academy": "https://www.khanacademy.org/math",
            "Paul's Online Math Notes": "http://tutorial.math.lamar.edu/",
            "Desmos": "https://www.desmos.com/",
            "Wolfram Alpha": "https://www.wolframalpha.com/",
            "PatrickJMT": "https://www.youtube.com/user/patrickJMT",
            "Art of Problem Solving": "https://artofproblemsolving.com/",
            "Project Euler": "https://projecteuler.net/",
            "The Math Learning Center": "https://www.mathlearningcenter.org/"
        },
        "English": {
            "Grammarly": "https://www.grammarly.com/",
            "Purdue OWL": "https://owl.purdue.edu/",
            "BBC Bitesize": "https://www.bbc.co.uk/bitesize/subjects/zckwqty",
            "SparkNotes": "https://www.sparknotes.com/",
            "TED-Ed": "https://ed.ted.com/"
        },
        "Software Engineering": {
            "W3Schools": "https://www.w3schools.com/",
            "GeeksforGeeks": "https://www.geeksforgeeks.org/",
            "FreeCodeCamp": "https://www.freecodecamp.org/",
            "MDN Web Docs": "https://developer.mozilla.org/en-US/",
            "Codecademy": "https://www.codecademy.com/",
            "GitHub": "https://github.com/"
        },
        "Enterprise Computing": {
            "IBM SkillsBuild": "https://www.ibm.com/training/skillsbuild",
            "Oracle Academy": "https://academy.oracle.com/",
            "Microsoft Learn": "https://learn.microsoft.com/en-us/",
            "AWS Educate": "https://aws.amazon.com/education/awseducate/"
        },
        "Other Useful Resources": {
            "EdX": "https://www.edx.org/",
            "Coursera": "https://www.coursera.org/",
            "OpenStax": "https://openstax.org/",
            "CrashCourse (YouTube)": "https://www.youtube.com/user/crashcourse",
            "YouTube EDU": "https://www.youtube.com/education",
            "TED Talks": "https://www.ted.com/talks",
            "Library Genesis": "https://libgen.is/",
            "Google Scholar": "https://scholar.google.com/",
            "Academic Earth": "https://academicearth.org/",
            "Study.com": "https://www.study.com/",
            "Skillshare": "https://www.skillshare.com/",
            "LinkedIn Learning": "https://www.linkedin.com/learning/",
            "Memrise": "https://www.memrise.com/",
            "Socratic": "https://www.socratic.org/",
            "Open Culture": "https://www.openculture.com/",
            "ChatGPT": "https://chatgpt.com/"
        }
    }


def format_links(links):
   # Formats a dictionary of categorized links into a structured, colored string for display. 
    display_link = ""  # Initialize an empty string to store the formatted links
    for category, sites in links.items():  # Loop through each category of links
        display_link += "\n" + MainColor2(category) + "\n"  # Add category name with color

        def add_sites(prefix, sites_dict):
          # Recursively processes the nested dictionary of sites, adding them with proper indentation.
            nonlocal display_link  # Allows modification of the display_link variable from the outer scope
            for i, (site, url) in enumerate(sites_dict.items()):  # Loop through each site in the category
                if isinstance(url, dict):  # Check if the URL is another dictionary (nested structure)
                    display_link += f"{prefix}├─ {red + site}\n"  # Add site name with color
                    add_sites(prefix + "│   ", url)  # Recursively call for nested links
                else:
                    if i == len(sites_dict) - 1:  # If it's the last site in the list, use '└─' (final branch)
                        display_link += f"{prefix}└─ {red + site}: {white + url}" + "\n"
                    else:  # Otherwise, use '├─' to indicate more items follow
                        display_link += f"{prefix}├─ {red + site}: {white + url}" + "\n"
        add_sites("", sites)  # Start processing the category sites

    return display_link  # Return the formatted string of links
# Call the function to format the links and store the result
formatted_links = format_links(links)
# Display the formatted links using slow animated text with color formatting
Slow(study + MainColor2(formatted_links))
# Handle any errors that might occur during execution
except Exception as e:
    print(f'{red}error: {purple}{e}')  # Print error message with color formatting

