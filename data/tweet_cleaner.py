import re
import pandas as pd

inputPath = "hateval2019_en_dev.csv"
outputPath = "hateval2019_en_dev_clean.csv"

data = pd.read_csv(inputPath)

print('Before CLeaning:')
print(data.head(10))

regex_pat = re.compile("@[A-Za-z0-9_-]+", flags=re.IGNORECASE)
data['text'] = data['text'].replace(regex_pat, '@USER')

print('After Cleaning:')
print(data.head(10))

data.to_csv(outputPath)
print('Created file! ' + outputPath)