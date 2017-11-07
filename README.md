# Data-Visualisation-Facebook-Chat
Python Script to visualise your facebook chat with a person

# Steps: 
## It requires that you have requested a copy of your data from facebook.(facebook settings -> general -> download a copy of your data)
- Your chat will be in a HTML file.
- createdataset.py will generate the required csv files.
  - chatdata.csv contains "date of sent messages"
  - count.csv contains "count of messages on a particular day" in unsorted manner
  - sorted.csv contains sorted data sorted in ascending order of date
- Only run plotdata.py.It will create the dataset and show the result

# Result:
![Output](https://github.com/Anupam-dagar/Data-Visualisation-Facebook-Chat/blob/master/plot.png?raw=true)

## Dependencies
- Pandas
- Numpy
- Matplotlib
- Python-tk
- Beautiful Soup
