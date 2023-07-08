import os
import requests
import json

x = int(input("Enter Atomic Number: "))

url = f"https://neelpatel05.pythonanywhere.com/element/atomicnumber?atomicnumber={x}"

r = requests.get(url)
print(r.text)

ChemDic = json.loads(r.text)

name = ChemDic["name"]
AtomicNo = ChemDic["atomicNumber"]
MassNO = ChemDic["atomicMass"]
Bp = ChemDic["boilingPoint"]
Mp = ChemDic["meltingPoint"]
Discovery = ChemDic["yearDiscovered"]
State = ChemDic["standardState"]
# Bonding = ChemDic["bondingType"]
GroupBlock = ChemDic["groupBlock"]
OxdnState = ChemDic["oxidationStates"]

os.system(f"say Element Name is : {name}. Atomic Number of this element is {AtomicNo} and Mass number is {Mp} .This element is found in {Discovery} period. Generally this element occured in {State} state.")

os.system(f"say Boiling point of this element is {Bp} and melting point of this element is {Mp}. This element is generally found in {GroupBlock} elements. And has oxidation state as {OxdnState}")
