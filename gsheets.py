import asyncio, random, os, gspread, discord
from oauth2client.service_account import ServiceAccountCredentials as SAC

def open():
    global sheet
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    creds = SAC.from_json_keyfile_name("Duck072Bot.json", scope)
    cliente = gspread.authorize(creds)
    sheet = cliente.open("Splat Hub Profile").sheet1
    return sheet

def read():
    sheet = open()
    flat_list = [item for sublist in sheet.get_all_values() for item in sublist]

def addrank(rank):
    sheet = open()
    listie = read()
    listie.append(rank)
    for counter, value in enumerate(listie):
        sheet.update_acell(f"A{str(counter)}",value)

def delrank(rank):
    sheet = open()
    listie = read()
    sheet.update_acell(f"A{str(len(listie))}","")
    listie.remove(rank)
    for counter, value in enumerate(listie):
        sheet.update_acell(f"A{str(counter)}",value)

