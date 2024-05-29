import polars as pl

path = r'/home/Park/workspace/github.com/ricebiceps/meet_the_hoteliers/'

# Read the CSV file into a Polars DataFrame with specific encoding and error handling
try:
    df = pl.read_csv(
        f'{path}/data/hotels.csv',
        encoding='utf8',  # You can change this if the file uses a different encoding
        infer_schema_length=10000,
        ignore_errors=True
    )
    
    # Drop the "Description" column
    df = df.drop(" Description")
    
    # Filter the DataFrame
    df_filtered = df.filter(pl.col(" countyName") == "Canada")
    
    # Add row index if the DataFrame is not empty
    if df_filtered.height > 0:
        df_filtered = df_filtered.with_row_count("row_index")
    
    # Write the filtered DataFrame to a new CSV file
    df_filtered.write_csv(f'{path}/data/hotel_data_canada.csv', separator=",")
    
    # Display the first 5 rows of the filtered DataFrame
    print(df_filtered.head(5))
    
except Exception as e:
    print(f"An error occurred: {e}")
