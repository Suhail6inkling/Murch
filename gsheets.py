import asyncio, random, os, gspread, discord
from oauth2client.service_account import ServiceAccountCredentials as SAC

def open():
    global sheet
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    creds = SAC.from_json_keyfile_name("Duck072Bot.json", scope)
    cliente = gspread.authorize(creds)
    sheet = cliente.open("Splat Hub Profile").sheet1

def read():
    return sheet.get_all_records()

def lenrows():
    return sheet.row_count

def updatecell(varchar, place: str, variable):
    global sheet
    listie = {"switchcode" : "C", "gender" : "D", "skincolour" : "E", "eyecolour" : "F", "hairstyle": "G", "trousers": "H", "weapon": "I", "level": "J", "sz": "K", "tc": "L", "rm": "M", "cb": "N",
              "hat": "O", "hatmain": "P", "hatsub1": "Q", "hatsub2": "R", "hatsub3" : "S",
              "shirt": "T", "shirtmain": "U", "shirtsub1": "V", "shirtsub2": "W", "shirtsub3": "X",
              "shoes": "Y", "shoesmain": "Z", "shoessub1": "AA", "shoessub2": "AB", "shoessub3": "AC"}

    column = listie[varchar]
    placebat = "{}{}".format(column,place)
    sheet.update_acell(placebat, variable)
    if varchar=="gender":
        column = listie["hairstyle"]
        placebat = "{}{}".format(column,place)
        sheet.update_acell(placebat, "None")

def delrow(index):
    global sheet
    sheet.delete_row(index)

def addrow(values):
    global sheet
    sheet.append_row(values)
    
