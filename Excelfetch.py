
import pandas as pd
import time
import openpyxl

# file_path = "Testcases.xlsx"
file_path = "StandardTestData.xlsx"

def fetch_executable_testcases(path,status='Y'):
    # Fetch the excel as Dataframe and filter the records based on mentioned criteria
    tc = pd.read_excel(path)
    tc_execute = tc.loc[tc['Execute'].str.upper() == status]
    # print(tC_execute)
    return tc_execute

new_test_date = fetch_executable_testcases(file_path)
print(new_test_date)
new_test_date.to_excel("new_StandardTestData.xlsx", index=False)

//Add a comment
counter=0
for counter in range(3):
	print (1)
	time.sleep(5)
	counter=counter+1
print ("Hi")