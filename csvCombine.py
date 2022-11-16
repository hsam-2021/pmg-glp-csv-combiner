import pandas as pd
import argparse
import csv
import sys
import os
import glob


def is_valid_file(parser, input_csv_files):
    # Ensure that the input_file exists.
    for csv_file in input_csv_files:
        if not os.path.exists(csv_file):
            parser.error("The file '{}' does not exist!".format(csv_file))
            sys.exit(1)


def is_valid_input_csv(parser, input_csv_files, column_limit):
    # Ensure that the # of rows in the input_file is greater than the row_limit.
    for csv_file in input_csv_files:
        col_count = 0
        df = pd.read_csv(csv_file)
        col_count = len(df.axes[1])
        if column_limit > col_count:
            parser.error("The 'column_limit' of '{}' is > the number of columns in '{}'!".format(col_count, csv_file))
            sys.exit(1)
        elif column_limit < col_count:
            parser.error("The 'column_limit' of '{}' is < the number of columns in '{}'!".format(col_count, csv_file))
            sys.exit(1)


# to check that only .csv files are read
def is_valid_output_csv(parser, output_file):
    filename, file_extension = os.path.splitext(output_file)
    if file_extension != '.csv':
        parser.error("Only csv file allowed for output")
        sys.exit(1)


# make df from csv files
def combined_csv(csv_files):
    dfs = []
    for file in csv_files:
        temp_df = pd.DataFrame()
        file_name = os.path.basename(file)
        topic = file_name.split('.')[0]
        data = pd.read_csv(file)
        data['filename'] = os.path.basename(topic)
        dfs.append(data)
        temp_df = pd.concat(dfs, ignore_index=True)
    combined_df_csv = pd.concat(dfs, ignore_index=True)

    return combined_df_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, nargs='+', required=True)
    parser.add_argument('--output_file', type=str, required=True)
    parser.add_argument('--matchColNum', type=int, required=True)
    args = parser.parse_args()
    # Check if the input_file exits
    is_valid_file(parser, args.input_file)
    # Check if the input_file is valid
    is_valid_input_csv(parser, args.input_file, args.matchColNum)
    # Check if the output_file name is valid
    is_valid_output_csv(parser, args.output_file)
    # get list of csv file as input_file argument
    output_csv_df = combined_csv(args.input_file)
    # to remove non-word characters for some data
    output_csv_df['category'] = output_csv_df['category'].str.replace('\W', '', regex=True)
    # write output csv to csv files
    with open(args.output_file, 'w') as f:
        output_csv_df.to_csv(f, encoding='utf-8', escapechar='\\', doublequote=False, index=False, line_terminator='\n')


if __name__ == "__main__":
    main()
