import pandas as pd
from AccDatasetEngine import AccData
from GenericDatasetEngine import GenData
import subprocess
import sys
import os

os.system("mode con cols=50 lines=50")

def Start():
     print("")
     print("  <<<<<<<<<<<<<<<</ \>>>>>>>>>>>>>>>>")
     print("       SPEAR ANTIPHISHING SOFTWARE     ")
     print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")



Start()
# Step 2: Read Spreadsheet Data
df = pd.read_excel("Roles1.xlsx")  # Update the path to your spreadsheet

# Step 3: Correlate Names with Roles
name_role_dict = dict(zip(df["Name"], df["Role"]))

# Step 4: User Input
name = input('Name:')

# Look up role based on entered name
if name in name_role_dict:
    role = name_role_dict[name]
    print(f"Role: {role}")
    print()
    if role == 'Accountant':
        AccData()
    elif role == 'IT Admin' or'Help Desk':
        GenData()
    
else:
    print("Name not found in the database.")
    subprocess.call([sys.executable, 'Roles Test.py'])
