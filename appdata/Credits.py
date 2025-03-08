from rich.console import Console
from rich.panel import Panel        #So much i could have done with rich but i don't know what 
import time
import requests

console = Console()  #console function from somewhere in richs files


#sends me users feedback if they have any
WEBHOOK = "https://discord.com/api/webhooks/1342459198738530356/_C7tE93oc0XcLbXeIf7n4QR9zc5bXsuFYIHqplL3SBokc0zaNv9BmN0UY6gzDIlyCudD"

def animated_list(items, delay=0.1):
    """Prints an animated list with bullet points.

    
    
    spaces for planning something:
    - make the best terminal app!
    
    """
    for item in items:
        console.print(f"[cyan]• {item}[/]", justify="left")
        time.sleep(delay)

def send_feedback(feedback):
    if not feedback.strip():
        console.print("[bold red]No feedback provided😭. Returning to menu.[/]")
        return
#push content to webhook
    data = {"content": f"📢 **User Feedback**:\n{feedback}"}
    response = requests.post(WEBHOOK, json=data)

    if response.status_code == 204:
        console.print("[bold green]✅ Feedback sent successfully![/]")
    else:
        console.print("[bold red]❌ Failed to send feedback.[/] Please try again later.")

def show_credits():
    console.clear()
    console.print(Panel.fit("[bold magenta]Cyan - Multi-tool for Students[/]", style="cyan"))
    console.print("\n[bold green]Developed by:[/] Amit Singh\n", justify="left")

    contributions = [
        "Lead Developer: Amit Singh",
        "GitHub: [link=https://github.com/Airstriker123]github.com/Airstriker123[/link] 🚀", #my github with other projects
        "Design & UX: Amit Singh",
        "Programming: Amit Singh",
        "Tested on 3 computers 💯" 
    ]
    animated_list(contributions)

    console.print("\n[italic yellow]Thank you for using Cyan![/]\n")

    feedback = console.input("[bold cyan]Got feedback? Type it here (or press Enter to skip): [/]")
    send_feedback(feedback)
#function is for cyan.py i know it is not needed but if it works I am not touching it    
def credits():
    show_credits()
