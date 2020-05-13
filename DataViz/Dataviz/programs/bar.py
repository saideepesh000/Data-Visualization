
from scraper import *
df2= pd.DataFrame(df)
print(df2)
df2.sort_values(by=['Tag_Count'],ascending=False).head(10).set_index('Technology').plot(kind='bar')
plt.title('10 Most Tagged Technologies On Stackoverflow.com')
plt.show()
