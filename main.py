# ==========================================
# Escape The Lab
# Created by Kaito-Comp
# ==========================================

inventory = []
current_room = "Cell"
toolbox_open = False
game_over = False


def show_inventory():
    print("\n========== INVENTORY ==========")
    if inventory:
        for item in inventory:
            print("- " + item)
    else:
        print("Empty")
    print("===============================\n")


def help_menu():
    print("""
================ COMMANDS ================

look room
look <object>

search <object>

take <item>

use <item> on <object>

open <object>

read <object>

enter <code>

inventory

help

quit

==========================================
""")


print("=" * 50)
print("              ESCAPE THE LAB")
print("=" * 50)
print("You slowly wake up on a cold metal floor.")
print("Your head hurts.")
print("You remember nothing.")
print("Escape the laboratory.\n")

help_menu()

while not game_over:

    command = input(f"\n[{current_room}] > ").lower().strip()

    if command == "quit":
        print("You gave up.")
        break

    elif command == "help":
        help_menu()

    elif command == "inventory":
        show_inventory()

    # =========================
    # CELL
    # =========================

    elif current_room == "Cell":

        if command.startswith("look"):

            if "room" in command:
                print("""
You are inside a small prison cell.

You see:
- A rusty bed
- A loose air vent
- A locked metal door
""")

            elif "bed" in command:
                print("An old rusty bed. Something is hidden underneath.")

            elif "vent" in command:
                print("The vent is attached with four screws.")

            elif "door" in command:
                print("The metal door is locked tight.")

            else:
                print("You don't notice anything special.")

        elif command.startswith("search"):

            if "bed" in command:
                if "Screwdriver" not in inventory:
                    print("You find a screwdriver hidden under the mattress.")
                else:
                    print("You already searched the bed.")

            else:
                print("You find nothing useful.")

        elif command.startswith("take"):

            if "screwdriver" in command:
                if "Screwdriver" not in inventory:
                    inventory.append("Screwdriver")
                    print("You picked up the screwdriver.")
                else:
                    print("You already have it.")

            else:
                print("You can't take that.")

        elif command.startswith("use"):

            if "screwdriver" in command and "vent" in command:

                if "Screwdriver" in inventory:
                    print("""
You remove the screws.

The vent falls open.

You crawl into the next room...
""")
                    current_room = "Storage Room"

                else:
                    print("You don't have a screwdriver.")

            else:
                print("That doesn't work.")

        else:
            print("Unknown command. Type 'help' if you're stuck.")
    # =========================
    # STORAGE ROOM
    # =========================

    elif current_room == "Storage Room":

        if command.startswith("look"):

            if "room" in command:
                print("""
You enter a dusty storage room.

You see:
- A metal toolbox
- A heavy security door
- Some shelves
""")

            elif "toolbox" in command:
                print("The toolbox looks old and tightly shut.")

            elif "door" in command:
                print("The security door has a keycard reader.")

            elif "shelves" in command:
                print("The shelves are covered in junk.")

            else:
                print("You don't notice anything special.")

        elif command.startswith("open"):

            if "toolbox" in command:

                if "Screwdriver" in inventory:

                    if not toolbox_open:
                        toolbox_open = True
                        print("You force the toolbox open.")

                    else:
                        print("The toolbox is already open.")

                else:
                    print("You need something to pry it open.")

            else:
                print("You can't open that.")

        elif command.startswith("search"):

            if "toolbox" in command:

                if toolbox_open:

                    if "Keycard" not in inventory:
                        print("Inside the toolbox is a blue keycard.")
                    else:
                        print("The toolbox is empty.")

                else:
                    print("The toolbox is closed.")

            else:
                print("You find nothing useful.")

        elif command.startswith("take"):

            if "keycard" in command:

                if toolbox_open:

                    if "Keycard" not in inventory:
                        inventory.append("Keycard")
                        print("You picked up the keycard.")

                    else:
                        print("You already have it.")

                else:
                    print("You don't see a keycard.")

            else:
                print("You can't take that.")

        elif command.startswith("use"):

            if "keycard" in command and "door" in command:

                if "Keycard" in inventory:
                    print("""
You swipe the keycard.

ACCESS GRANTED.

The security door slides open.
""")
                    current_room = "Control Room"

                else:
                    print("You don't have a keycard.")

            else:
                print("That doesn't work.")

        else:
            print("Unknown command. Type 'help' if you're stuck.")
    # =========================
    # CONTROL ROOM
    # =========================

    elif current_room == "Control Room":

        if command.startswith("look"):

            if "room" in command:
                print("""
You step into the control room.

You see:
- A computer
- A desk
- A sticky note
- A keypad beside the EXIT door
""")

            elif "computer" in command:
                print("The computer is locked with a password.")

            elif "desk" in command:
                print("A small metal desk. A sticky note rests on it.")

            elif "note" in command:
                print("Maybe you should read it.")

            elif "keypad" in command:
                print("The keypad is waiting for a 3-digit code.")

            elif "door" in command:
                print("A huge reinforced exit door.")

            else:
                print("You don't notice anything special.")

        elif command.startswith("search"):

            if "desk" in command:
                print("Apart from the sticky note, there's nothing useful.")

            elif "room" in command:
                print("Nothing else catches your attention.")

            else:
                print("You find nothing useful.")

        elif command.startswith("read"):

            if "note" in command:
                print("""
========================
 EMERGENCY EXIT NOTICE
========================

Exit Code: 427

Do not share this code.
""")

            else:
                print("You can't read that.")

        elif command.startswith("enter"):

            if "427" in command:
                print("""
The keypad beeps.

ACCESS GRANTED.

The exit door unlocks.
""")
                current_room = "Exit"

            else:
                print("The keypad flashes red.")
                print("Incorrect code.")

        else:
            print("Unknown command. Type 'help' if you're stuck.")
    # =========================
    # EXIT
    # =========================

    elif current_room == "Exit":

        print("""
==================================================
                    FREEDOM
==================================================

You slowly push against the heavy exit door.

With a loud hiss...

The locking bolts slide back.

Fresh air rushes into the laboratory.

You sprint outside into the sunlight.

Congratulations!

You escaped the laboratory!
""")

        print("Final Inventory:")
        show_inventory()

        print("""
================= GAME COMPLETE =================

Thanks for playing Escape The Lab!

Type 'yes' to play again, or anything else to quit.
""")

        choice = input("> ").lower().strip()

        if choice == "yes":
            inventory.clear()
            current_room = "Cell"
            toolbox_open = False
            print("\nStarting a new game...\n")
        else:
            game_over = True

    else:
        print("An unexpected error occurred.")
        game_over = True
print("""
=========================================
        Thanks for Playing!
=========================================

Created by Kaito-Comp

Ideas for future updates:
- More rooms
- More puzzles
- Random keypad codes
- Save/Load system
- Multiple endings
- Colored terminal text

Good luck escaping again!
=========================================
""")
