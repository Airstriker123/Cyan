import calendar
from datetime import datetime
from colors_app import *
import fade

#var
y = datetime.now().year
m = datetime.now().month
d = int(datetime.now().strftime("%d"))
month_calendar = calendar.month(y, m).split("\n")

#ui elements
header = f""" 
 ██████╗ █████╗ ██╗     ███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║     ███████║██║     █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║     ██╔══██║██║     ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████╗██║ ╚████║██████╔╝███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                                               
{reset}
"""
faded_text = fade.water(header)
#current day show
for i in range(len(month_calendar)):
    if f"{d:2}" in month_calendar[i]:
        month_calendar[i] = month_calendar[i].replace(f"{d:2}", f"{green}{d:2}{red}")

print(faded_text)
print(f"{red}\n".join(month_calendar) + reset)

#options
print(f"\n{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"🌟 {yellow}Select an option below:{reset}")
print(f"{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}")
print(f"""
{cyan}1{reset}. 📌 Add a date to track {cyan}(highlighted in cyan){reset}
{cyan}2{reset}. 📋 Show tracked dates
{cyan}3{reset}. ❌ Delete all tracked dates
{cyan}4{reset}. 🗑  Delete a certain date
{cyan}5{reset}. 📝 Set a reminder for a task {yellow}(highlighted in yellow){reset}
{cyan}6{reset}. 🚪 Exit calendar
""")

input(f"{green}>>>{reset}")


