import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers interactively")

# Load data
df = pd.read_csv('metadata.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df_clean = df.dropna(subset=['title', 'publish_time'])

# Interactive widget: year range
year_range = st.slider("Select publication year range", int(df_clean['year'].min()), int(df_clean['year'].max()), (2020, 2021))

filtered_df = df_clean[(df_clean['year'] >= year_range[0]) & (df_clean['year'] <= year_range[1])]

st.subheader("Number of Papers by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color='skyblue')
st.pyplot(fig)

st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
ax2.barh(top_journals.index, top_journals.values, color='green')
st.pyplot(fig2)

st.subheader("Sample of Papers")
st.dataframe(filtered_df[['title', 'journal', 'year']].head(10))

# Word cloud
st.subheader("Word Cloud of Paper Titles")
text = ' '.join(filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)
