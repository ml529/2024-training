# -*- coding: utf-8 -*-

guests = ["Albert Einstein", "Ada Lovelace", "Leonardo da Vinci"]
unavailable_guest = "Albert Einstein"
new_guest = "Marie Curie"

print(f"\nUnfortunately, {unavailable_guest} is unable to attend.")

guests[guests.index(unavailable_guest)] = new_guest

for guest in guests:
    print(f"Dear {guest}, please join me for dinner.")