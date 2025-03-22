from rich.console import Console # using rich for tables
from rich.panel import Panel
import time
import requests
from rich.table import Table 

console = Console() #function from rich

#webhook url for sending feedback
WEBHOOK = "https://discord.com/api/webhooks/1342459198738530356/_C7tE93oc0XcLbXeIf7n4QR9zc5bXsuFYIHqplL3SBokc0zaNv9BmN0UY6gzDIlyCudD"

#function to print contributions
def animated_list(items, delay=0.1):
    for item in items:
        console.print(f"[cyan]• {item}[/]", justify="left")
        time.sleep(delay)
#function to submit feedback.
def send_feedback(feedback):
    if not feedback.strip():
        console.print("[bold red]No feedback provided😭. Returning to menu.[/]")
        return
    data = {"content": f"📢 **User Feedback**:\n{feedback}"}
    response = requests.post(WEBHOOK, json=data)
    if response.status_code == 204:
        console.print("[bold green]✅ Feedback sent successfully![/]")
    else:
        console.print("[bold red]❌ Failed to send feedback.[/] Please try again later.")
#main function 
def show_credits(): #everythigng that will be printed in terminal
    console.clear()
    console.print(Panel.fit("[bold magenta]Cyan - Multi-tool for Students[/]", style="cyan"))
    console.print("\n[bold green]Developed by:[/] Amit Singh\n", justify="left")

    contributions = [
        "Lead Developer: Amit Singh",
        "GitHub: [link=https://github.com/Airstriker123]github.com/Airstriker123[/link] 🚀",
        "Design & UX: Amit Singh",
        "Programming: Amit Singh",
        "Tested on 3 computers 💯"
    ]
    animated_list(contributions) #function printed

    # Create rich table for credits of modules used in project
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Modules Used", style="cyan")
    table.add_column("Use", justify="left", style="yellow")
    table.add_column("Link", justify="left", style="green")

    table.add_row("colorama", "Color support for console text", "https://pypi.org/project/colorama/")
    table.add_row("pytubefix", "Download YouTube videos (patched pytube)", "https://github.com/fent/node-ytdl-core")
    table.add_row("pydub", "Audio processing (conversion, editing)", "https://github.com/jiaaro/pydub")
    table.add_row("ffmpeg", "Multimedia processing (audio/video)", "https://ffmpeg.org/")
    table.add_row("imageio[ffmpeg]", "Read/write images & videos", "https://imageio.readthedocs.io/")
    table.add_row("fade", "Adds fading effects to text in CLI", "https://pypi.org/project/fade/")
    table.add_row("Flask", "Web framework for Python", "https://flask.palletsprojects.com/")
    table.add_row("requests", "Handles HTTP requests", "https://docs.python-requests.org/")
    table.add_row("rich", "Better CLI app, tables, text formatting", "https://github.com/Textualize/rich")
    table.add_row("PyExecJS", "Run JavaScript from Python", "https://pypi.org/project/PyExecJS/")
    table.add_row("datetime", "Handles date and time operations", "https://docs.python.org/3/library/datetime.html")
    table.add_row("simplejson", "Extended JSON handling", "https://pypi.org/project/simplejson/")
    table.add_row("jsons", "Serialize/deserialize JSON data", "https://pypi.org/project/jsons/")
    table.add_row("pypi-json", "Retrieve package metadata from PyPI", "https://pypi.org/project/pypi-json/")
    table.add_row("textblob", "NLP (Natural Language Processing)", "https://pypi.org/project/textblob/")
    table.add_row("pyspellchecker", "Spell checking in Python", "https://pypi.org/project/pyspellchecker/")
    table.add_row("sympy", "Symbolic mathematics library", "https://www.sympy.org/")

    console.print(table)
    console.print("\n[italic yellow]Thank you for using Cyan![/]\n")

    feedback = console.input("[bold cyan]Got feedback? Type it here (or press Enter to skip): [/]")
    send_feedback(feedback)

#function for cyan.py
def credits():
    show_credits()
