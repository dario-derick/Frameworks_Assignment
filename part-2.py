# Convert date columns to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year from publish_time
df['year'] = df['publish_time'].dt.year

# Handle missing values (example: drop rows without title)
df_clean = df.dropna(subset=['title', 'publish_time'])

# Create additional columns, e.g., abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').apply(lambda x: len(x.split()))
