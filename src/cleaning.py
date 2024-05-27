import polars as pl

path = r'/home/Park/workspace/github.com/ricebiceps/meet_the_grocers/'

# Read the CSV file into a Polars DataFrame with specific encoding and error handling
try:
    df = pl.read_csv(
        f'{path}/data/hotels.csv',
        encoding='utf8',  # You can change this if the file uses a different encoding
        infer_schema_length=10000,
        ignore_errors=True
    )
    # Display the first 5 rows
except Exception as e:
    print(f"An error occurred: {e}")

df = df.filter(pl.col(" countyName") == "Canada")
row_count = df.with_row_index()

df.write_csv(f'{path}/data/hotel_data_canada.csv', separator=",")