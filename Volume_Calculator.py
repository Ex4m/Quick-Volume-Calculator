import numpy as np
import pandas as pd
import keyboard as key

# Create an empty DataFrame
quant = []
length = []
width = []
height = []
named_columns ={"Quantity": quant,
                "Lenght": length,
                "Width": width,
                "Height": height}

df = pd.DataFrame(named_columns)

def df_style (val):
        return "font-weight: bold"
while True:
    # Get user input for dimensions
    quant = input("Enter how many cartons: ")
    length = input("Enter length: ")
    width = input("Enter width: ")
    height = input("Enter height: ")

    # Convert the dimensions to numeric values
    quant = float(quant)
    length = float(length)
    width = float(width)
    height = float(height)

    # Create new row as dictionarz and then convert it to dataframe which can be concatenate afterwards with existing dataframe
    new_row = {"Quantity":quant,"Lenght":length,"Width":width,"Height": height}
    new_row = pd.DataFrame([new_row])
    df = pd.concat([df, new_row], ignore_index=True)
    print(df)


    more = input("Do you want to add more dimensions? y/n: ")
    if more.lower() != "y" :#or more == key.is_pressed("enter"):
        break

df["cbm"] = df["Quantity"] * df["Lenght"] * df["Width"] * df["Height"] / 1000000
df["vol_weight_167"] = df["Lenght"] * df["Width"] * df["Height"] * 167 / 1000000
total = df.loc["TOTAL"] = df.sum(numeric_only= True, axis = 0)
df.style.applymap(df_style,total)
print(df)

save_it = input("Do you wish to save this as .csv ? y/n: ")
if save_it.lower() == "y":
    df.to_csv("vol.csv",index = False)
    print("file saved")

save_it_ex = input("and do you wish to save it as excel file ? y/n: ") # musí být nainstalovaný pip install openpyxl
if save_it_ex.lower() == "y":
    df.to_excel("vol.xlsx", index=False, sheet_name='Sheet1', header=True)
    print("file saved")
print("That´s all folks, bye")