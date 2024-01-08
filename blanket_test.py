import os
import re
import pandas as pd


store_path= 

store_files = os.listdir(store_path)


def sort_files():

    customer_files = []
    transaction_files = []
    do_not_send = []
    all_other = []

    for file in store_files:
        file_name = file.lower()
        if re.search("not",file_name):
            do_not_send.append(file_name)
        elif re.search("customer",file_name):
            customer_files.append(file_name)
        elif re.search("transaction", file_name):
            transaction_files.append(file_name)
        else:
            all_other.append(file_name)

    return customer_files,transaction_files


def compare_columns_list(cust_list):

    df_1_columns = []
    df_2_columns = []

    for i in range(len(cust_list) - 1):  
        print(i)

        file_path_1 = store_path  + f'/{cust_list[i]}'
        df_1 = pd.read_csv(file_path_1)

        file_path_2 = store_path  + f'/{cust_list[i + 1]}'
        df_2 = pd.read_csv(file_path_2)

        for col in df_1.columns:
            df_1_columns.append(col)
        for col in df_2.columns:
            df_2_columns.append(col)

        if df_1_columns != df_2_columns:
            return {"Error 1": "Columns do not match"}
            return 1
    return "Success"
            

def combine_df(cust_list):

    all_cust_data = pd.DataFrame()

    for file in cust_list:
        file_path = store_path  + f'/{file}'
        cust_df = pd.read_csv(file_path)
        all_cust_data = all_cust_data.append(cust_df, ignore_index=True)
    return all_cust_data

#compare all columns name is the same across
#check and count rows for each column


def validation_check_1(cust_data):

    null_counts = cust_data.isnull().sum()
    all_counts = cust_data.count()
    print(null_counts)
    print(all_counts)



def warning_notes(notes):

    all_notes =[]

    all_notes.append(notes)





def main():
    
    cust_file, trans_file = sort_files()
    compare_columns_result=compare_columns_list(cust_file)
    if compare_columns_result != "Success":
        warning_notes(compare_columns_result)
    cust_data =combine_df(cust_file)
    validation_check_1(cust_data)

if __name__ == "__main__":
    main()






        






    
