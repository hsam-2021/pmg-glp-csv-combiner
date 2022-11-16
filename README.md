# CSV Combiner
This command line program will take several CSV files as arguments and output a new csv file that has all the rows from each of the input csv files along with additional column that has the filename from which the row came.
## Set up enviroment
```bash
python3.9 -m venv venv && source venv/bin/activate && pip install -U pip setuptools wheel
pip install -r requirements.txt
```

## Run csvCombine.py

```bash

 python csvCombine.py --input_file fixtures/accessories.csv fixtures/clothing.csv fixtures/household_cleaners.csv --output_file csv_combined.csv --matchColNum 2
```

## Output
- Output file is saved in csv_combined.csv
## Run Unit Tests

```bash

 python -m unittest test_csvCombine.py
 
 or 
 
 python -m unittest discover
```