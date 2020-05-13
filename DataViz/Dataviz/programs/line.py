
from scraper import *
df3= pd.DataFrame(df,columns=['Technology','Tag_Count']).head(10)
print(df3)
df3.plot(x='Technology',y='Tag_Count',kind='line')
plt.title('10 Most Tagged Technologies On Stackoverflow.com')
plt.show()

