from selenium import webdriver



"""
webtable - static and dynamic
following tags for table - 
<table>
    <thead>
    </thead>
    <tbody>
        <tr>
            <td>data</td>
            <td>data</td>
        </tr>
        <tr> </tr>
        <tr> </tr>
    </tbody>
</table>
table - craete table
tbody - table data is under this 
th - header of table
tr - tble row
td - table data
 
mostly used customized xpath/dynamic xpath
1) count number of rows and columns
2) read specific row and column data
3) read all the rows nd column data -->
 # parameterizing value into xpath
//table[@name='BookTable']//tbody//tr[5]//td[1]" -->"//table[@name='BookTable']//tbody//tr["+str(r)+"]//td["+str(c)+"]"

4) read data based on condition

"""
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
# 1) count number of rows and columns
no_of_rows = len(driver.find_elements("xpath","//table[@name='BookTable']//tr"))
no_of_columns = len(driver.find_elements("xpath","//table[@name='BookTable']//th"))
print(no_of_columns,no_of_rows) #4 7

# how to read specific row and column data
data = driver.find_element("xpath","//table[@name='BookTable']//tbody//tr[5]//td[1]").text
print(data)

# read all rows and columns
for r in range(2,no_of_rows+1):
    for c in range(1,no_of_columns+1):
        driver.find_element("xpath","")
        # parameterizing value into xpath
        data = driver.find_element("xpath", "//table[@name='BookTable']//tbody//tr["+str(r)+"]//td["+str(c)+"]").text
        print(data,end='                ')
    print()

# read data based on condition
for r in range(2,no_of_rows+1):
    auther_name=driver.find_element("xpath","//table[@name='BookTable']//tbody//tr["+str(r)+"]//td[2]").text
    if auther_name=='mukesh':
        book_name = auther_name = driver.find_element("xpath", "//table[@name='BookTable']//tbody//tr[" + str(r) + "]//td[1]").text
        print(book_name,"         ",auther_name)



