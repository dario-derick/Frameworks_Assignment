import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# Publications by year
year_counts = df_clean['year'].value_counts().sort_index()
plt.figure(figsize=(10,5))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# Top journals
top_journals = df_clean['journal'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
plt.title("Top Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()

# Word cloud of titles
text = ' '.join(df_clean['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Distribution of paper counts by source
plt.figure(figsize=(10,5))
df_clean['source_x'].value_counts().head(10).plot(kind='bar')
plt.title("Paper Count by Source")
plt.xlabel("Source")
plt.ylabel("Number of Papers")
plt.show()
