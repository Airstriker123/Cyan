import calendar
import time
from datetime import datetime
import fade
import os
import sys
from rich.console import Console
from rich.table import Table
from colors_app import *

if sys.platform.startswith("win"):
    os_name = "Windows"
elif sys.platform.startswith("linux"):
    os_name = "Linux"
else:
    os_name = "Unknown"
def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")


Clear()
console = Console()

# Get current date details (Australian format)
today = datetime.now()
y, m, d = today.year, today.month, today.day

# Generate calendar
month_calendar = calendar.month(y, m).split("\n")

# UI elements
header = """ 
 ██████╗ █████╗ ██╗     ███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║     ███████║██║     █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║     ██╔══██║██║     ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████╗██║ ╚████║██████╔╝███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                                               
"""
faded_text = fade.water(header)


# Highlight current day in the calendar
for i in range(len(month_calendar)):
    if f"{d:2}" in month_calendar[i]:
        month_calendar[i] = month_calendar[i].replace(f"{d:2}", f"{green}{d:2}{red}")

# Tracked assessments storage (Australian format: DD-MM-YYYY)
tracked_assessments = []


def display_calendar():
    print(faded_text)
    print(f'{red}\n'.join(month_calendar) + reset)

    # Display tracked assessments in a table
    if tracked_assessments:
        table = Table(title="📚 Tracked Assessments")
        table.add_column("Assessment Name", style="bold magenta")
        table.add_column("Due Date (DD-MM-YYYY)", style="cyan")
        table.add_column("Reminder", style="yellow")
        for assessment in sorted(tracked_assessments, key=lambda x: x["date"]):
            table.add_row(assessment["name"], assessment["date"], assessment["reminder"])
        console.print(table)


def add_tracked_assessment():
    name = input("Enter assessment name: ").strip()
    date = input("Enter due date (DD-MM-YYYY): ").strip()

    try:
        datetime.strptime(date, "%d-%m-%Y")  # Validate date format
        reminder = input("Enter a reminder: ").strip()
        tracked_assessments.append({"name": name, "date": date, "reminder": reminder})
        console.print("[green]Assessment added successfully![/green]")
    except ValueError:
        console.print("[red]Invalid date format! Please use DD-MM-YYYY.[/red]")


def show_tracked_assessments():
    if not tracked_assessments:
        console.print("[red]No assessments tracked![/red]")
    else:
        display_calendar()


def delete_all_tracked_assessments():
    tracked_assessments.clear()
    console.print("[red]All tracked assessments deleted.[/red]")


def delete_tracked_assessment():
    date = input("Enter due date to delete (DD-MM-YYYY): ").strip()
    for assessment in tracked_assessments:
        if assessment["date"] == date:
            tracked_assessments.remove(assessment)
            console.print("[green]Assessment removed successfully![/green]")
            return
    console.print("[red]Assessment not found![/red]")


def main():
    while True:
        display_calendar()
        print(f"\n🌟 Select an option below:")
        print(f"{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}")
        print(f"""
{cyan}[{reset}1{cyan}]{reset} 📌 Add an assessment to track
{cyan}[{reset}2{cyan}]{reset} 📋 Show tracked assessments
{cyan}[{reset}3{cyan}]{reset} ❌ Delete all tracked assessments
{cyan}[{reset}4{cyan}]{reset} 🗑  Delete a certain assessment
{cyan}[{reset}5{cyan}]{reset} 🚪 Exit calendar
{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}
""")

        choice = input(f"{green}>>>{reset} ").strip()


        if choice == "1":
            add_tracked_assessment()
        elif choice == "2":
            show_tracked_assessments()
        elif choice == "3":
            delete_all_tracked_assessments()
        elif choice == "4":
            delete_tracked_assessment()
        elif choice == "5":
            console.print("[red]Exiting...[/red]")
            break
        else:
            console.input("[red]Invalid choice! [!]press enter to continue[!][/red]")
            Clear()



if __name__ == "__main__":
    main()

