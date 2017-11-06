# Data-Visualisation-Facebook-Chat
Python Script to visualise your facebook chat with a person

# Steps: 
## It requires that you have requested a copy of your data from facebook.(facebook settings -> general -> download a copy of your data)
- Your chat will be in a HTML file.
- First run create-dataset.py.It will generate the required csv files.
  - chatdata.csv contains "date of sent messages"
  - count.csv contains "count of messages on a particular day" in unsorted manner
  - sorted.csv contains sorted data sorted in ascending order of date
- Finally run plotdata.py to get the result

## Dependencies
- Pandas
- Numpy
- Matplotlib
- Python-tk
- Beautiful Soup
