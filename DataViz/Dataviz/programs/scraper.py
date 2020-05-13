import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style

df = {'Technology':[],'Tag_Count':[]}



def extract_tagged(url):
    #print('Extracting Content')
    content = requests.get(url)
    soup = BeautifulSoup(content.text,'html.parser')
     
    for tag in soup.find_all('a',attrs={'class':'post-tag'}):
        df['Technology'].append(tag.text)
    for count in soup.find_all('span',attrs={'class':'item-multiplier-count'}):
        df['Tag_Count'].append(count.text)
    
for i in range(1,3):
    extract_tagged('http://stackoverflow.com/tags?page='+str(i)+'&tab=popular')    
    df['Tag_Count']=[int(i) for i in df['Tag_Count']]

#style.use('ggplot')
s=pd.DataFrame(df).head(40)
print(s)








