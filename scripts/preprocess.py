from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import nltk

nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

# Get stopwords
stop_words_english = stopwords.words('english')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def preprocess_text(text: str) -> str:
  """
  Performs classic text preprocessing steps:
  - Lowercase conversion
  - Removal of punctuation
  - Removal of stopwords
  - Lemmatization
  """
  # Lowercase conversion
  text = text.lower()

  # Remove punctuation
  punc = ['.', ',', '"', '!', '?', ':', ';', '(', ')', '[', ']', '{', '}']
  for p in punc:
    text = text.replace(p, '')

  # Tokenize the text
  words = text.split()

  # Remove stopwords
  words = [word for word in words if word not in stop_words_english]

  # Lemmatize words
  lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

  # Join words back into a string
  return ' '.join(lemmatized_words)
