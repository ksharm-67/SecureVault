from pickle import *
import os
from AESencryption import *

def storeInVault(new_entry: list):
    entries = []
    if os.path.exists('storage.vault'):
        with open('storage.vault', 'rb') as file:
            try:
                entries = load(file)
            except EOFError:
                entries = []
    
    entries.append(new_entry)
    with open('storage.vault', 'wb') as file:
        dump(entries, file)

def createVault():
    with open('storage.vault', 'wb') as file:
        dump([], file)

def readVault(service: str):
    matches = []
    if not os.path.exists('storage.vault'):
        return matches

    with open('storage.vault', 'rb') as file:
        try:
            entries = load(file)
            for entry in entries:
                if entry[0] == service:
                    matches.append((entry[1], entry[2]))
        except Exception:
            pass

    return matches

def delRecord(rec: str):
    entries = []
    if os.path.exists('storage.vault'):
        with open('storage.vault', 'rb') as file:
            try:
                entries = load(file)
            except EOFError:
                entries = []

    new_entries = [entry for entry in entries if entry[1] != rec]

    with open('storage.vault', 'wb') as file:
        dump(new_entries, file)

def viewAll(master: str, salt: bytes):
    if not os.path.exists('storage.vault'):
        print("No vault found.")
        return

    with open('storage.vault', 'rb') as file:
        try:
            entries = load(file)
            for entry in entries:
                print(f"For service {entry[0]}, Username: {entry[1]}, and Password: {decryptPwd(entry[2], master, salt)}")
        except Exception:
            print("Vault is empty or unreadable.")

def checkVault():
    try:
        with open('storage.vault', 'rb') as file:
            load(file)
        return True
    except Exception as e:
        print("Exception:", e)
        return False
