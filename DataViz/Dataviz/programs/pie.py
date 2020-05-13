
from scraper import *

df4= pd.DataFrame(df,columns=['Technology','Tag_Count']).head(20)
print(df4)
df4.plot(labels=df['Technology'],y='Tag_Count',kind='pie',legend=False,autopct='%1.1f%%',startangle=90)
plt.title('20 Most Tagged Technologies On Stackoverflow.com')
plt.show()

