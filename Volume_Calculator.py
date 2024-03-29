import pandas as pd
import keyboard as key
import time
import logo as lg
import winsound
import random

response = ["y","yes","yap","yeah",","]
clip_loc_2 = "C:/Users/Exa/Documents/GitHub/Quick-Volume-CalculatorMotley-Crue-Kickstart-my-Heart_logo"
clip_loc = "C:/Users/Exa/Downloads/Motley-Crue-Kickstart-my-Heart_logo"
 
 
#Starting loading screen
ran_list = ["Fetching up the final numbers for you !","Go ahead -- hold your breath!","Please wait while the little elves draw your map",
            "My other loading screen is much faster.","Just count to 10","Creating time-loop inversion field",
            "Spinning the wheel of fortune...", "Please wait until the sloth starts moving.","Don't break your screen yet!",]    
pick_one = random.choice(ran_list)     
ran_list.remove(pick_one)    
pick_second = random.choice(ran_list)


def start_seq():
    """Starting seq which is showing the logo and some cool music to enhace and motivate for quick calculation :)

    Args:
        skip (str): Bool - response on user input defined in response
    """
    skip = input("Do you want to skip the main logo? y/n: ")    
    if skip not in response:
        winsound.PlaySound(clip_loc, winsound.SND_ASYNC)   
        print(pick_one)
        time.sleep(5)
        print(pick_second)  
        time.sleep(5)                                                                                                                                                                                                                                                                    
        lg.print_logo(0.07) 
    else:
        print("So, my hard work on a fancy logo is not enough for you Ha? :) \n")
    
  
start_seq()


print("\033[1mEx4m v. 1.4\033[0m\n\n")
                                                                                                                                                     
print( """Hi,
This is \033[1m Quick Volume Calculator\033[0m and this should work as helptool for creating a quick sheets of data used for example in logistics with various outputs.
please use this responses to navigate if you want to advance to next section: "y","yes","yap","yeah", or ","\n\n """)                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                  
# Create an empty DataFrame
quant = []
length = []
width = []
height = []
weight= []

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


# Definition for customs func.
def format_values(value):
    """Formating values in a way that will replace entries of "," with ".". Also let you repair input if it was used as wrong type

    Args:
        value (not_specified): User input which than is evaulated and ideally transfered to float

    Returns:
        value: Return formated value of the entry input
    """
    try:
        value = float(value)
        return value
    except ValueError:
        try:
            value = value.replace(",",".")
            value = float(value)
            return value
        except ValueError:
            while True:
                try:
                    value = input("Invalid input, Please enter a value, not a text: ")
                    value = value.replace(",",".")
                    value = float(value)
                    return value
                except:
                    continue

def Repair_table(used_df, repair_it):
    """Repair function which will specify the dimensions of the matrix and then rewrite it´s value

    Args:
        used_df (pandas.core.frame.DataFrame): used dataframe to repair within
        repair_it (str): string of responses 

    Returns:
        _type_: _description_
    """
    if repair_it.lower() in response:
        print("\n\n\n------------Actual REPAIRED table ----------")
        print(used_df)
        print("\n Now tell me dimensions which you wish to change")
        first_dim = int(input("Tell me first dimension of the matrix - i.e. order num. of the row: "))
        second_dim = int(input("Tell me second dimension of the matrix - i.e. order num. of the column: "))
        value = format_values(input("What value you would like to write there: "))
        used_df.iat[first_dim,second_dim] = value
        print("\n")
        print(used_df)
        return True
    else:
        return False
    
    
    
weight_inp = input("do you wish to include weight columns? y/n: ")        
while True:
    # Get user input for dimensions
    quant = format_values(input("Enter how many cartons: "))
    length = format_values(input("Enter length: "))
    width = format_values(input("Enter width: "))
    height = format_values(input("Enter height: "))
            
    if weight_inp in response:
        weight = format_values(input("Enter weight: "))
        

    # Create new row as dictionary and then convert it to dataframe which can be concatenate afterwards with existing dataframe
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
    print("\n\n\n--------------RESULT-----------------")
    print(df)
    
def add_packing(row):
    """Function which will evaulate wheter is the dimensions provided suitable more for pallet or carton

    Args:
        row (row): each row of the df

    Returns:
        str: what kind of string to apply to Packing column as output
    """
    if (row["Length [1]"] >= 80 and row["Width [2]"] >= 60) or (row["Length [1]"] >= 60 and row["Width [2]"] >= 80):
        return "plt"
    else:
        return "ctn"
    
if weight_inp in response:
    df2_orig = pd.DataFrame.copy(df2)
    df2["Packing"] = df2.apply(add_packing, axis=1)
    df2["Volume"] = df2["Quantity [0]"] * df2["Length [1]"] * df2["Width [2]"] * df2["Height [3]"] / 1000000
    df2["Total Weight"] = df2["Quantity [0]"]*df2["Weight [4]"]
    df2["Volumetric weight (167*cbm)"] = df2["Volume"] * 167

    columns_for_sum =["Quantity [0]","Volume","Total Weight","Volumetric weight (167*cbm)"]
    total = df2.loc["TOTAL"] = df2[columns_for_sum].sum(numeric_only= True, axis = 0, skipna = True)
    print("\n\n\n--------------RESULT-----------------")
    print(df2) 



#Save the output to different formats
save_it = input("Do you wish to save this as .csv ? y/n: ")
if save_it.lower() in response:
    if weight_inp not in response:
        df.to_csv("vol.csv",index = False)
    else:
        df2.to_csv("vol.csv",index = False)
    print("file saved as vol.xlsx")

save_it_ex = input("and do you wish to save it as excel file ? y/n: ") # musí být nainstalovaný pip install openpyxl
if save_it_ex.lower() in response:
    if weight_inp not in response:
        df.to_excel("vol.xlsx", index=False, sheet_name='Sheet1', header=True)
    else:
        df2.to_excel("vol.xlsx", index=False, sheet_name='Sheet1', header=True)
    print("file saved as vol.xlsx")

save_it_2 = input("Do you wish to save it in excel organized for copying? y/n: ")
if save_it_2.lower() in response:
    if weight_inp not in response:
        df_orig = df_orig.applymap(lambda x: int(x) if type(x) == float and x == round(x) else x)
        #new column and conversion to one line which is printable
        df_orig["len_Wi_Hei"] = df_orig.apply(lambda x: f'{x["Quantity [0]"]}x  {x["Length [1]"]}x{x["Width [2]"]}x{x["Height [3]"]} cm', axis=1)
        df_orig["len_Wi_Hei"].to_excel("vol2.xlsx", index=False, sheet_name='Sheet1', header=True)
        print("file saved as Vol2.xlsx")
    else:
        df2_orig = df2_orig.applymap(lambda x: int(x) if type(x) == float and x == round(x) else x)
        #new column and conversion to one line which is printable
        df2_orig["len_Wi_Hei_Wei"] = df2_orig.apply(lambda x: f'{x["Quantity [0]"]}x  {x["Length [1]"]}x{x["Width [2]"]}x{x["Height [3]"]} cm  {x["Weight [4]"]} kg/', axis=1) 
        df2["Packing"] = df2.apply(lambda x: f'{x["Packing"]}',axis=1 )
        df2_orig = df2_orig.assign(Packing=df2["Packing"], blank1=["----"]* len(df2_orig), blank2=["----"]* len(df2_orig), Volume=df2["Volume"], Weight=df2["Weight [4]"])
        df2_orig["len_Wi_Hei_Wei_Pack"] = df2_orig.apply(lambda x: f'{x["Quantity [0]"]}x  {x["Length [1]"]}x{x["Width [2]"]}x{x["Height [3]"]} cm  {x["Weight [4]"]} kg/{x["Packing"]}', axis=1)
        df2_orig["Total Weight"] = df2_orig["Quantity [0]"] * df2_orig["Weight [4]"]
        cols_for_sum =["Volume","Total Weight"]
        total = df2_orig.loc["TOTAL"] = df2_orig[cols_for_sum].sum(numeric_only= True, axis = 0, skipna = True)
        df2_orig[["Volume","Total Weight","----","----","len_Wi_Hei_Wei_Pack"]].to_excel("vol2.xlsx", index=False, sheet_name='Sheet1', header=True)
        print("file saved as Vol2.xlsx")
        

print("That´s all folks, bye")