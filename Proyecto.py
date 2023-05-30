#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas
import numpy
tweets_csv = pandas.read_csv('tweets.csv', header=None,
                       names=['index', 'id', 'date', 'query',
                              'user', 'message'])


# In[17]:


# Número de filas y columnas
print(tweets_csv.shape)


# In[18]:


# 10 primeras filas
tweets_csv.head(10)


# In[4]:


import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer


# In[19]:


# en el pdf pone que la funcion se llame asi
def limpiar_texto(tweet):
                
    # Eliminar menciones, hashtags y URLs
    tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)  # Eliminar menciones
    tweet = re.sub(r'#', '', tweet)  # Eliminar hashtags
    tweet = re.sub(r'http\S+|www\S+', '', tweet)  # Eliminar URLs
    
    # Eliminar símbolos extraños
    tweet = re.sub(r'\W', ' ', tweet)  # Eliminar caracteres no alfanuméricos
    
     # Convertir a minúsculas
    tweet = tweet.lower()
    
    # Tokenización
    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(tweet)
    
    # Eliminar stop words
    stop_words = set(stopwords.words('english'))  # stop word para mensajes en ingles
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lematización (stemming)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Unir tokens nuevamente en un solo texto
    tweet_cleaned = ' '.join(tokens)
        
    return tweet_cleaned


# In[20]:


# Escribe los valores en un archivo de texto
with open('tweets_message.txt', 'w') as file:
    for value in tweets_csv.iloc[:, -1]:
        file.write(str(value) + '\n') # Escribe los mensajes del csv en un txt


# In[21]:


# Abre el archivo en modo lectura
with open('tweets_message.txt', 'r') as file:
    # Lee el contenido del archivo
    tweets_txt = file.read()

print(tweets_txt)


# In[22]:


cleaned_tweets= [] 
with open('tweets_message.txt', 'r') as file:
    for line in file:
        cleaned_tweet = limpiar_texto(line)
        cleaned_tweets.append(cleaned_tweet)
        print(cleaned_tweet)


# In[23]:


cleaned_tweets


# In[12]:


import csv
from textblob import TextBlob


# In[24]:


# con polaridad
classified_tweets = []

for line in cleaned_tweets:
    blob = TextBlob(line)
    polaridad = blob.sentiment.polarity
    
    if polaridad > 0.4:
        label = 'Muy feliz'
        
    elif polaridad > 0:
        label = 'Contento'
    elif polaridad == 0:
        label = 'Neutro'
    elif polaridad > -0.4:
        label = 'Molesto'
    else:
        label = 'Hater'
    
    classified_tweets.append([line, label])

# Guardar los resultados en un archivo CSV
with open('classified_tweets.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['tweet', 'label'])
    writer.writerows(classified_tweets)


# In[15]:


# con valor de las etiquetas, no usa textBlob y quieren q lo usemos asi q asi no es.
# Lo podemos usar para el paso 4, para validar y corregir los datos
# (este es mortal hacerlo de 0 pq habria que poner muchos valores en cada etiqueta, pero el de arriba tiene fallitos aunq en general va bien)
labels = {
    'Muy feliz': ['happy', 'cheerful', 'excited'],
    'Contento': ['glad', 'satisfied', 'pleasant'],
    'Neutro': ['neutral', 'indifferent', 'normal'],
    'Molesto': ['annoying', 'angry', 'cry'],
    'Hater': ['hate', 'negative', 'critical']
}

classified_tweets = []

for line in cleaned_tweets:
    label = 'Neutro' # neutro por defecto
    
    for current_label, valuesOfLabels in labels.items():
        if any(valuesOfLabels in line for valuesOfLabels in valuesOfLabels):
            label = current_label
            break
    
    classified_tweets.append([line, label])

# Guardar los resultados en un archivo CSV
with open('classified_tweets2.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['tweet', 'label'])
    writer.writerows(classified_tweets)


# In[ ]:




