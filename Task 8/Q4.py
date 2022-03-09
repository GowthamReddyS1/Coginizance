import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
NewSeries = ser.str.title()
print(NewSeries)