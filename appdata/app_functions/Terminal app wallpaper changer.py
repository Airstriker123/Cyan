import json
import os
from colors_app import *

def change_windows_terminal_background(image_path):
    settings_path = os.path.expanduser(
        r"~\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")

    if not os.path.exists(settings_path):
        print(f"❌{red} Error: Windows Terminal settings file not found.")
        return


    with open(settings_path, "r", encoding="utf-8") as file:
        settings = json.load(file)


    default_profile_guid = settings.get("defaultProfile")


    profiles_list = settings.get("profiles", {}).get("list", [])
    if not profiles_list:
        print(f"❌{red} Error: No profiles found in settings.json.")
        return

    changed = False
    default_profile_found = False


    for profile in profiles_list:
        if "backgroundImage" not in profile:
            print(f"🛠{green} Adding background settings to profile: {profile.get('name', 'Unnamed Profile')}")

        profile["backgroundImage"] = image_path
        profile["backgroundImageStretchMode"] = "uniformToFill"
        profile["backgroundImageOpacity"] = 0.8
        changed = True


        if profile.get("guid") == default_profile_guid:
            print("🎯 Updating default profile background.")
            profile["backgroundImage"] = image_path
            default_profile_found = True


    if default_profile_found:
        settings["profiles"]["defaults"]["backgroundImage"] = image_path

    if changed:

        with open(settings_path, "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)
        print(
            f"✅{green} Terminal background updated for all profiles and default profile! Restart Windows Terminal to see changes.")
    else:
        print(f"{red}⚠️ No changes were made.")



image_path = input(f"{purple}Enter full image path (PNG, JPG, GIF): ").strip()
change_windows_terminal_background(image_path)
#DO NOT STEAL MY CODE MONKEY!!!!!