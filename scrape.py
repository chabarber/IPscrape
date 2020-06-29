############################################
#Script Name    :scrape.py
#Description      :basic scrapping tool
#Args                 :none
#Author              :Chase Barber
#Email               :nope
############################################

#Imports used:
    #Beautfiful Soup: HTML Web Parser
    #re: Regex For Python
    #requests: library to access webpages
from bs4 import BeautifulSoup
import re
import requests

#these 3 variables are for collecting an address and accessing the HTML and parsing it
url = "https://www.proxynova.com/proxy-server-list/elite-proxies/"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

#this is for searching through the HTML for a class "table" that then has all of the IP's stored in a <script> tag
table = content.find("table", attrs={"class": "table"})
table_ip = table.find_all("script")
table_port = table.find_all("td")

#this opens and creates a file called proxies.txt
file1 = open("proxies.txt", "w")

# this for loop iterates through the script tags to append them as strings then a regex line that is less than 53 characters is written to the file with the count then incremented
converted_data = []
ip_list = []
count = 0

for i in table_ip:
    converted_data.append(str(i))
    if(len(converted_data[count]) < 53):
        file1.writelines(re.findall(r'[0-9]+(?:\.[0-9]+){3}', converted_data[count]))
        file1.write("\n")
    count += 1

file1.close()
    
