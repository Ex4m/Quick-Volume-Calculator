import numpy as np
import pandas as pd
import keyboard as key

# Create an empty DataFrame
quant = []
length = []
width = []
height = []
weight= []
response = ["y","yes","yap","yeah",","]
named_columns ={"Quantity": quant,
                "Lenght": length,
                "Width": width,
                "Height": height}
named_columns_w_weight = {"Quantity": quant,
                          "Lenght": length,
                          "Width": width,
                          "Height": height,
                          "Weight": weight,
                          "----": []}
df = pd.DataFrame(named_columns)
df2 = pd.DataFrame(named_columns_w_weight)

def df_style (val):
        return "font-weight: bold"

weight_inp = input("do you wish to include weight columns? y/n: ")        
while True:
    # Get user input for dimensions
    quant = input("Enter how many cartons: ")
    length = input("Enter length: ")
    width = input("Enter width: ")
    height = input("Enter height: ")
    if weight_inp in response:
        weight = input("Enter weight: ")
    # Convert the dimensions to numeric values
    quant = float(quant)
    length = float(length)
    width = float(width)
    height = float(height)
    try:
        weight = float(weight)
    except:
        pass
    # Create new row as dictionarz and then convert it to dataframe which can be concatenate afterwards with existing dataframe
    if weight_inp not in response:
        new_row = {"Quantity":quant,"Lenght":length,"Width":width,"Height": height}
        new_row = pd.DataFrame([new_row])
        df = pd.concat([df, new_row], ignore_index=True)
        print(df)
    if weight_inp in response:
        new_row_weight = {"Quantity":quant,"Lenght":length,"Width":width,"Height": height,"Weight": weight, "----": []}
        new_row_weight = pd.DataFrame([new_row_weight])
        df2 = pd.concat([df2, new_row_weight], ignore_index=True)
        print(df2)


    more = input("Do you want to add more dimensions? y/n: ")
    if  more.lower() not in response:
        break


if weight_inp not in response:
    df["Volume"] = df["Quantity"] * df["Lenght"] * df["Width"] * df["Height"] / 1000000
    df["Volumetric weight (167/cbm)"] = df["Lenght"] * df["Width"] * df["Height"] * 167 / 1000000
    columns_for_sum =["Quantity","Volume","Volumetric weight (167/cbm)"]

    total = df.loc["TOTAL"] = df[columns_for_sum].sum(numeric_only= True, axis = 0, skipna = True)
    df.style.applymap(df_style,total)
    print(df)
if weight_inp in response:
    df2["Volume"] = df2["Quantity"] * df2["Lenght"] * df2["Width"] * df2["Height"] / 1000000
    df2["Total Weight"] = df2["Quantity"]*df2["Weight"]
    df2["Volumetric weight (167/cbm)"] = df2["Lenght"] * df2["Width"] * df2["Height"] * 167 / 1000000

    columns_for_sum =["Quantity","Volume","Total Weight","Volumetric weight (167/cbm)"]
    total = df2.loc["TOTAL"] = df2[columns_for_sum].sum(numeric_only= True, axis = 0, skipna = True)
    df2.style.applymap(df_style,total)
    print(df2) 

save_it = input("Do you wish to save this as .csv ? y/n: ")
if save_it.lower() in response:
    if weight_inp not in response:
        df.to_csv("vol.csv",index = False)
    else:
        df2.to_csv("vol.csv",index = False)
    print("file saved")

save_it_ex = input("and do you wish to save it as excel file ? y/n: ") # musí být nainstalovaný pip install openpyxl
if save_it_ex.lower() in response:
    if weight_inp not in response:
        df.to_excel("vol.xlsx", index=False, sheet_name='Sheet1', header=True)
    else:
        df2.to_excel("vol.xlsx", index=False, sheet_name='Sheet1', header=True)
    print("file saved")

print("That´s all folks, bye")