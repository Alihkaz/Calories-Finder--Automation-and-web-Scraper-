
#imports 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



# ____________________________________________________________________________________________________

# Constants:


nutritionvalue_link="https://www.nutritionvalue.org/Pasta%2C_enriched%2C_dry_nutritional_value.html"





chrome_driver_path="Your chrome driver path "







# _________________________________________ Setting up the driver ! ___________________________________________________________

Food_search=input("What food you want to search calories for?\n ")

driver=webdriver.Chrome()  #setting up the driver 

driver.get(nutritionvalue_link)                                #getting the website we want to scrap 

driver.implicitly_wait(15)           #waiting for 15 second                                                 #waiting 5 seconds before we continue


# _________________________________________Sending the data that the user wants to search for !___________________________________________________________


search_button= driver.find_element(By.XPATH,'//*[@id="main"]/tbody/tr[1]/td/div[1]/a[2]') #searching for the search button

search_button.click()          #clicking on it   

driver.implicitly_wait(15)           #waiting for 15 second


input_box= driver.find_element(By.ID,'search-box') #searching for the input box 

input_box.send_keys(Food_search)   #searcing for the food entered by the user !

input_box.send_keys(Keys.ENTER)

driver.implicitly_wait(15)           #waiting for 15 second


# _________________________________________getting the data that the user searched for !___________________________________________________________


table_choices=driver.find_elements(By.CLASS_NAME,'table_item_name')

choices=[ element.get_attribute('innerHTML') for element in table_choices] #extracting all the choices available and presenting them to the user to choose from ,
                                                                           #and later onn we will choose from the table depending on what the user have choosed !



user_input=int(input(f"{choices}\n please specify which type of {Food_search} you want by selecting the number corresponding to it !"))-1

user_choice=driver.find_element(By.PARTIAL_LINK_TEXT,f"{choices[user_input]}") #searching for the  choice of the user


driver.implicitly_wait(40)           #waiting for 40 second

user_choice.click()   #clicking on the first_choice

driver.implicitly_wait(40)           #waiting for 40 second




# _________________________________________Organizing and manipulating those data in the google forms !___________________________________________________________


#every thing is working normally , except when an advertisment appears,
#  the details of element which we click on will not appear , and we cant extract the calories info ,
#  but if an advertisement doesn't appear , the following code will work normally , and the calories will be extracted,
# i will try in the future to improve this code , and solve the bug !  



calories_nutrition_facts=driver.find_element(By.XPATH,'/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]')

driver.implicitly_wait(40)           #waiting for 40 second


calories=calories_nutrition_facts.get_attribute('innerHTML')
   


print(calories)

