from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome()

"""
how to handle cookies - 
test our application is creating cookie or not?
every cookie having some attribute such as -
name
value
expirydate
also every cookie having its value
it will store in one dictionary so it considered as one cookie

how to add cookie -
add in the form of dictionary


"""


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

#capture cookies from the browser
cookies = driver.get_cookies()
print(len(cookies)) #3

# #print details of all cookies
# for i in cookies:
#     # print(i)
#     print(i.get('name'),"",i.get("value"))

# add new cookie to the browser
driver.add_cookie({"name":"Mycookie","value":"1234"})
cookies = driver.get_cookies()
print(len(cookies))

# delete specific cookie from the browser
driver.delete_cookie("Mycookie")
cookies = driver.get_cookies()
print(len(cookies))
#  delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))





