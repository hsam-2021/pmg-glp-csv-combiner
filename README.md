# CSV Combiner
This command line program will take several CSV files as arguments and output a new csv file that has all the rows from each of the input csv files along with additional column that has the filename from which the row came.
## Set up enviroment
Python3 required
```bash
pip install -r requirements.txt
```

### Run csvCombine.py

* **--input_file**  :     list of input csv files
* **--output_file** :   single output csv file
* **--matchColNum** :  Validation to match number of columns in all input CSV files are same 

```bash

 python csvCombine.py --input_file fixtures/accessories.csv fixtures/clothing.csv fixtures/household_cleaners.csv --output_file csv_combined.csv --matchColNum 2
```

### Output
- Output file is saved as **csv_combined.csv**
### Run Unit Tests

```bash

 python -m unittest test_csvCombine.py
 
 or 
 
 python -m unittest discover
```
### Known issue
When running in Ubuntu20.04 LTS (using Python 3.8.10):

![img.png](img.png)

So if you are testing on Linux machine, just replace “line_terminator” with “lineterminator” on line 70 (csvCombine.py)