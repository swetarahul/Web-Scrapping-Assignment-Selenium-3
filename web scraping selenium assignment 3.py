#!/usr/bin/env python
# coding: utf-8

# In[88]:


#1. write python program which take take input from user. e.g guitar


# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


# In[20]:


driver=webdriver.Chrome(r"C:\Users\msi 1\Downloads\chromedriver_win32\chromedriver.exe")
#connect to the driver


# In[21]:


# Opening Amazon.in in chrome browser
url='http://www.amazon.in/'
driver.get(url)
time.sleep(2)


# In[22]:


# Taking input from user about product search
User_input=input('Enter the title of Product you are interest in search :')


# In[24]:


Search=driver.find_element(By.XPATH,'//input[@id="twotabsearchtextbox"]')


# In[25]:


# clearing any previous input in search bar
Search.clear()


# In[26]:


# Feeding input specified by user to search menu through send keys
Search.send_keys(User_input)


# In[27]:


# Finding Search button for clicking through xpath
Search_button=driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]')


# In[28]:


# Clicking search button
Search_button.click()


# In[166]:


#2. In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in df and csv.details to be scrapped are "brand",

   


# In[29]:


b_name=[]
product_name=[]
rating=[]
no_of_rating=[]
price=[]
ret_exchange=[]
exp_delivery=[]
availability=[]
other_details=[]
product_url=[]
urls=[]


# In[56]:


for i in range(0,3):
    if i>2:
        break
    p_urls=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in p_urls:
        urls.append(i.get_attribute('href'))


# In[57]:


for i in urls:
       driver.get(i)
       time.sleep(2)


# In[69]:


#scraping data for brand name
try:
    bran=driver.find_element(By.XPATH,"//a[@id='bylineInfo']")
    b_name.append(bran.text)
except NoSuchElementException as e:
    b_name.append("--")


# In[70]:


#scraping data for product name
try:
   prod=driver.find_element(By.XPATH,"//h1[@id='title']/span")
   product_name.append(prod.text)
except NoSuchElementException as e:
   product_name.append("--")


# In[71]:


#scraping data for rating
try:
   rat=driver.find_element(By.XPATH,"//span[@id='acrPopover']/span/a/i/span")
   rating.append(rat.text)
except NoSuchElementException as e:
   rating.append("--")


# In[72]:


#scraping data for rating no.
try:
   rat_no=driver.find_element(By.XPATH,"//span[@id='acrCustomerReviewText']")
   no_of_rating.append(rat_no.text)
except NoSuchElementException as e:
   no_of_rating.append("--")


# In[73]:


#scraping data for price
try:
   pri=driver.find_element(By.XPATH,"//div[@id='apex_desktop']/div/div/table/tbody/tr[2]/td[2]/span/span[2]")
   price.append(pri.text)
except NoSuchElementException as e:
   price.append("--")


# In[74]:


#scaping data for return
try:
    retu=driver.find_element(By.XPATH,"//div[@id='RETURNS_POLICY']/span/div[2]/a")
    ret_exchange.append(retu.text)
except NoSuchElementException as e:
    ret_exchange.append("--")


# In[75]:


#scraping data for expected delivery
try:
   deliv=driver.find_element(By.XPATH,"//div[@id='ddmDeliveryMessage']/b")
   exp_delivery.append(deliv.text)
except NoSuchElementException as e:
   exp_delivery.append("--")


# In[76]:


#scraping data for availability
try:
   avail=driver.find_element(By.XPATH,"//div[@id='availability']/span")
   availability.append(avail.text)
except NoSuchElementException as e:
   availability.append("--")


# In[77]:


#scraping data for other details
try:
   od=driver.find_element(By.XPATH,"//div[@id='feature-bullets']/ul/li/span")
   other_details.append(od.text)
except NoSuchElementException as e:
   other_details.append("--")


# In[78]:


# selecting and clicking next page
try:
   if i==1:
       n_button=driver.find_element(By.XPATH,"//div[@class='a-section a-spacing-none a-padding-base']/div/ul/li[3]/a")
       n_url=n_button.get_attribute('href')
       driver.get(n_url)
       time.sleep(2)
except:
   if i==2:
       n_button=driver.find_element(By.XPATH,"//div[@class='a-section a-spacing-none a-padding-base']/div/ul/li[4]/a")
       n_url=n_button.get_attribute('href')
       driver.get(n_url)


# In[79]:


#Placing everything into dataframe
df=pd.DataFrame(list(zip(b_name,product_name,rating,no_of_rating,price,ret_exchange,exp_delivery,availability,other_details,urls)),columns=["Brand Name","Product","Rating","No. of rating","Price","Return/Exchange","Expected Delivery","Availability","Other Details","Product Url"])
df


# In[ ]:


#3. n images.google.com and scrape 10 images of fruits.


# In[18]:


driver=webdriver.Chrome(r"C:\Users\msi 1\Downloads\chromedriver_win32\chromedriver.exe")
#connect to the driver


# In[20]:


url = "https://images.google.com/"
time.sleep(2)


# In[21]:


urls = []    
data = []
search_item = ["fruits", "cars", "Machine Learning","guitar","cakes"]


# In[26]:


for item in search_item:
    driver.get(url)  
    time.sleep(5)
    search_img=driver.find_element(By.XPATH,'//input[@class="gLFyf"]') #sending key word for search item
    


# In[27]:


search_img.send_keys(item)


# In[29]:


search_btn = driver.find_element(By.XPATH,'//button[@class="Tg7LZd"]') #Clicking on search button


# In[30]:


search_btn.submit()


# In[31]:


# scrolling the web page to get more images
for _ in range(20):
    driver.execute_script("window.scrollBy(0,1000)")


# In[33]:


imgs = driver.find_elements(By.XPATH,"//img[@class='rg_i Q4LuWd']")
img_url = []


# In[34]:


for image in imgs:
        source = image.get_attribute('src')
        if source is not None:
                if(source[0:4] == 'http'):
                    img_url.append(source)


# In[35]:


for i in img_url[:10]:
    urls.append(i)


# In[37]:


import requests
for i in range(len(urls)):
    if i > 10:
        break
    print("Downloading {0} of {1} images" .format(i, 10))
    response = requests.get(urls[i])


# In[ ]:


#4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand 
Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, 
“Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
details is missing then replace it by “- “. Save your results in a dataframe and CSV


# In[57]:


driver=webdriver.Chrome(r"C:\Users\msi 1\Downloads\chromedriver_win32\chromedriver.exe")
#connect to the driver


# In[78]:


driver.get("https://www.flipkart.com/")


# In[79]:


searchbar=driver.find_element(By.XPATH,'//input[@class="_3704LK"]')


# In[80]:


searchbar.send_keys("pixel 4A")


# In[83]:


searchButton=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
searchButton.click()


# In[90]:


flip_urls=[]
urls=driver.find_element(By.XPATH,('//a[@class="_1fQZEK"]'))


# In[ ]:


#5.Q5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps


# In[116]:


driver=webdriver.Chrome("chromedriver.exe") 
time.sleep(2)


# In[117]:


# opening google maps
url = "https://www.google.co.in/maps"
driver.get(url)
time.sleep(2)


# In[118]:


search = driver.find_element(By.ID,"searchboxinput") 


# In[119]:


search.clear()


# In[120]:


time.sleep(2)


# In[121]:


search.send_keys("New Delhi") 


# In[122]:


button = driver.find_element(By.ID,"searchbox-searchbutton")  


# In[123]:


button.click()


# In[124]:


try:
    url_str = driver.current_url
    print("URL Extracted: ", url_str)
    latitude_longitude = re.findall(r'@(.*)data',url_str)
    if len(latitude_longitude):
        lat_lng_list = latitude_longitude[0].split(",")
        if len(lat_lng_list)>=2:
            latitude = lat_lng_list[0]
            longitude = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(latitude, longitude))

except Exception as e:
        print("Error: ", str(e))


# In[125]:


#6. Write a program to scrap all the available details of best gaming laptops from digit.in.


# In[126]:


driver=webdriver.Chrome("chromedriver.exe") 
time.sleep(2)


# In[127]:


url = "https://www.digit.in/"
driver.get(url)
time.sleep(3)


# In[130]:


#searching for best laptop
best_gam_lap = driver.find_element(By.XPATH,"//div[@class='listing_container']//ul//li[9]").click()
time.sleep(4)


# In[131]:


#Creating empty lists
lap_name = []
ope_sys = []
display = []
processor = []
memory = []
weight = []
dimensions = []
graph_proc = []
price = []


# In[133]:


# Scraping the data of laptop names
name_tags = driver.find_elements(By.XPATH,"//table[@id='summtable']//tr//td[1]")
for name in name_tags:
    lap_name.append(name.text)


# In[136]:


#Scraping the data of operating system
try:
    os_tags = driver.find_elements(By.XPATH,"//div[@class='Spcs-details']//tr[3]//td[3]")
    for os in os_tags:
        ope_sys.append(os.text)
except NoSuchElementException:
    pass        


# In[137]:


#scraping display
try:
    disp_tags = driver.find_elements(By.XPATH,"//div[@class='Spcs-details']//tr[4]//td[3]")
    for disp in disp_tags:
        display.append(disp.text)
except NoSuchElementException:
    pass


# In[138]:


#Scraping data of Processor
try:
    pro_tags = driver.find_elements(By.XPATH,"//div[@class='Spcs-details']//tr[5]//td[3]")
    for pro in pro_tags:
        processor.append(pro.text)
except NoSuchElementException:
    pass


# In[139]:


#Scraping data of memory
try:
    memo_tags = driver.find_elements(By.XPATH,"//div[@class='Spcs-details']//tr[6]//td[3]")
    for memo in memo_tags:
        memory.append(memo.text)
except NoSuchElementException:
    pass


# In[140]:


#Scraping data of weight
try:
    wgt_tags = driver.find_elements(By.XPATH,"//div[@class='Spcs-details']//tr[7]//td[3]")
    for wgt in wgt_tags:
        weight.append(wgt.text)
except NoSuchElementException:
    pass


# In[141]:


#Scraping data of dimensions
try:
    dim_tags = driver.find_elements(By.XPATH,"//div[@class='Spcs-details']//tr[8]//td[3]")
    for dim in dim_tags:
        dimensions.append(dim.text)
except NoSuchElementException:
    pass


# In[143]:


#Scraping data of Graph processor
try:
    gra_tags = driver.find_elements(By.XPATH,"//div[@class='Spcs-details']//tr[9]//td[3]")
    for gra in gra_tags:
        graph_proc.append(gra.text)
except NoSuchElementException:
    pass


# In[144]:


#Scraping data of price
try:
    pri_tags = driver.find_elements(By.XPATH,"//td[@class='smprice']")
    for pri in pri_tags:
        price.append(pri.text.replace('₹','Rs '))
except NoSuchElementException:
    pass


# In[146]:


#Printing data frame
Gaming_Laptop


# In[150]:


# Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. 


# In[172]:


driver=webdriver.Chrome("chromedriver.exe") 
time.sleep(2)


# In[174]:


# opening web page
driver.get("https://www.forbes.com/billionaires/")
driver.maximize_window()
time.sleep(2)


# In[175]:


# Create Empty list
rank = []
name = []
net_worth = []
age = []
citzn = []
source = []
industry = []


# In[177]:


#Fetching Rank
rank_tag = driver.find_elements(By.XPATH,"//div[@class='rank']")
for r in rank_tag:
    try:
        rank.append(r.text)
    except NoSuchElementException:
        rank.append("-")


# In[178]:


#Fetching Name
name_tag = driver.find_elements(By.XPATH,"//div[@class='personName']")
for n in name_tag:
    try:
        name.append(n.text)
    except NoSuchElementException:
        name.append("-")


# In[179]:


#Fetching Net Worth
netwrth_tag = driver.find_elements(By.XPATH,"//div[@class='netWorth']")
for nt in netwrth_tag:
    try:
        net_worth.append(nt.text)
    except NoSuchElementException:
        net_worth.append("-")


# In[180]:


#Fetching Age
age_tag = driver.find_elements(By.XPATH,"//div[@class='age']")
for a in age_tag:
    try:
        age.append(a.text)
    except NoSuchElementException:
        age.append("-")


# In[181]:


#Fetching Citizenship
cit_tag = driver.find_elements(By.XPATH,"//div[@class='countryOfCitizenship']")
for c in cit_tag:
    try:
        citzn.append(c.text)
    except NoSuchElementException:
        citzn.append("-")


# In[182]:


#Fetching Source
src_tag = driver.find_elements(By.XPATH,"//span[@class='source-text']")
for s in src_tag:
    try:
        source.append(s.text)
    except NoSuchElementException:
        source.append("-")


# In[183]:


#Fetching Industry
ind_tag = driver.find_elements(By.XPATH,"//div[@class='category']")
for ind in ind_tag:
        try:
            industry.append(ind.text)
        except NoSuchElementException:
            industry.append("-")


# In[184]:


# Length of all the coloumns
len(rank),len(name),len(net_worth),len(age),len(citzn),len(source),len(industry)


# In[185]:


#create Dataframe
Billionaires =pd.DataFrame({'Rank':rank,'Name':name,'Net Worth':net_worth,'Age': age,'Citizenship/Country':citzn,'Source':source,'Industry':industry})
Billionaires


# In[186]:


# Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted from yt video


# In[187]:


driver=webdriver.Chrome("chromedriver.exe") 
time.sleep(2)


# In[188]:


driver.get("https://www.youtube.com/watch?v=USccSZnS8MQ")
driver.maximize_window()
time.sleep(2)


# In[190]:


i=0
while(i<100):
    driver.execute_script("window.scrollBy(0,500)") # scroll down to get more comments
    i+=1
while(i<402):
    driver.execute_script("window.scrollBy(0,5000)") # scroll down to get more comments
    i+=1


# In[191]:


comment = []
upvote = []
comment_time = []


# In[192]:


comment_tag=(driver.find_elements(By.XPATH,'//yt-formatted-string[@id="content-text"]'))
for i in comment_tag:             
    try:
        comment.append(i.text)
    except NoSuchElementException:
        comment.append("-")


# In[193]:


upvote_tag=(driver.find_elements(By.XPATH,"//*[@id='vote-count-middle']"))
for i in upvote_tag:             
    try:
        upvote.append(i.text)
    except NoSuchElementException:
        upvote.append("-")


# In[194]:


comment_time_tag=(driver.find_elements(By.XPATH,"//*[@id='header-author']/yt-formatted-string/a"))
for i in comment_time_tag:             
    try:
        comment_time.append(i.text)
    except NoSuchElementException:
        comment_time.append("-")


# In[195]:


video=pd.DataFrame({"Comment":comment,"Upvote":upvote,"Comment_ Time":comment_time})
video


# In[ ]:




