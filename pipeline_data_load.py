import pandas as pd
import import google.datalab.bigquery as bq


# Loading in the data from BigQuery or from file source.

#### BigQuery:  Create a function to call the bigquery data ####
def load_data_GBQ():
    try:
        data = requests.execute(output_options=bq.QueryOutput.dataframe()).result()
        print("Loaded data successfully from Google Big Query")
		return data
    except:
    		print("LOADING ERROR: Unable to load data from Google Big Query")


def load_data_file(file):
	try:
		data = pd.read_csv(file)
		print("Loaded data from file")
		return data
	except:
		print("LOAD ERROR: Unable to load data from file")
