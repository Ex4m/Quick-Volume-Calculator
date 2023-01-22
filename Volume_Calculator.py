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
named_columns ={"Quantity [0]": quant,
                "Length [1]": length,
                "Width [2]": width,
                "Height [3]": height}
named_columns_w_weight = {"Quantity [0]": quant,
                          "Length [1]": length,
                          "Width [2]": width,
                          "Height [3]": height,
                          "Weight [4]": weight,
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
        new_row = {"Quantity [0]":quant,"Length [1]":length,"Width [2]":width,"Height [3]": height}
        new_row = pd.DataFrame([new_row])
        df = pd.concat([df, new_row], ignore_index=True)
        print(df)
    if weight_inp in response:
        new_row_weight = {"Quantity [0]":quant,"Length [1]":length,"Width [2]":width,"Height [3]": height,"Weight [4]": weight, "----": []}
        new_row_weight = pd.DataFrame([new_row_weight])
        df2 = pd.concat([df2, new_row_weight], ignore_index=True)
        print(df2)


    more = input("Do you want to add more dimensions? y/n: ")
    if  more.lower() not in response:
        break

def Repair_table(used_df, repair_it):
    if repair_it.lower() in response:
        print("\n\n\n")
        print(used_df)
        print("\n Now tell me dimensions which you wish to change")
        first_dim = int(input("Tell me first dimension of the matrix - i.e. order num. of the row: "))
        second_dim = int(input("Tell me second dimension of the matrix - i.e. order num. of the column: "))
        value = float(input("What value you would like to write there: "))
        used_df.iat[first_dim,second_dim] = value
        print("\n")
        print(used_df)
        return True
    else:
        return False

repair_it = input("Do you wish to repair any value? y/n: ")
flag = False
if weight_inp in response:
    flag = Repair_table(df2,repair_it)
elif weight_inp not in response:
    flag = Repair_table(df,repair_it)


 
while flag:
    repair_it = input("Do you wish to repair any value? y/n: ")
    if weight_inp in response:
        flag = Repair_table(df2,repair_it)
    elif weight_inp not in response:
        flag = Repair_table(df,repair_it)
      

if weight_inp not in response:
    df_orig = pd.DataFrame.copy(df)
    df["Volume"] = df["Quantity [0]"] * df["Length [1]"] * df["Width [2]"] * df["Height [3]"] / 1000000
    df["Volumetric weight (167*cbm)"] = df["Length [1]"] * df["Width [2]"] * df["Height [3]"] * 167 / 1000000
    columns_for_sum =["Quantity [0]","Volume","Volumetric weight (167*cbm)"]

    total = df.loc["TOTAL"] = df[columns_for_sum].sum(numeric_only= True, axis = 0, skipna = True)
    df.style.applymap(df_style,total)
    print(df)
if weight_inp in response:
    df2_orig = pd.DataFrame.copy(df2)
    df2["Volume"] = df2["Quantity [0]"] * df2["Length [1]"] * df2["Width [2]"] * df2["Height [3]"] / 1000000
    df2["Total Weight"] = df2["Quantity [0]"]*df2["Weight [4]"]
    df2["Volumetric weight (167*cbm)"] = df2["Volume"] * 167

    columns_for_sum =["Quantity [0]","Volume","Total Weight","Volumetric weight (167*cbm)"]
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

save_it_2 = input("Do you wish to save it in excel organized for copying? y/n: ")
if save_it_2.lower() in response:
    if weight_inp not in response:
        df_orig = df_orig.applymap(lambda x: int(x) if type(x) == float and x == round(x) else x)
        #new column and conversion to one line which is printable
        df_orig["len_Wi_Hei"] = df_orig.apply(lambda x: f'{x["Quantity [0]"]}x  {x["Length [1]"]}x{x["Width [2]"]}x{x["Height [3]"]} cm', axis=1)
        df_orig["len_Wi_Hei"].to_excel("vol2.xlsx", index=False, sheet_name='Sheet1', header=True)
        print("file saved")
    else:
        df2_orig = df2_orig.applymap(lambda x: int(x) if type(x) == float and x == round(x) else x)
        #new column and conversion to one line which is printable
        df2_orig["len_Wi_Hei_Wei"] = df2_orig.apply(lambda x: f'{x["Quantity [0]"]}x  {x["Length [1]"]}x{x["Width [2]"]}x{x["Height [3]"]} cm  {x["Weight [4]"]} kg/', axis=1)
        df2_orig["len_Wi_Hei_Wei"].to_excel("vol2.xlsx", index=False, sheet_name='Sheet1', header=True)
        print("file saved")
        



print("That´s all folks, bye")