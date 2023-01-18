import pymongo
import pandas
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATABASE_NAME = "Application1"
COLLECTION_NAME = "Sensor1"
data_file_path = "/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__": 
   df= pandas.read_csv(data_file_path)
   print(f"Rows and Columns: {df.shape}") 
   df.reset_index(drop=True,inplace=True)
   
   # Convert dataframe to json so that we can dump these records in MONGODB
   json_record = list(json.loads(df.T.to_json()).values())
   print(json_record[0])

#insert converted json records to mongodb
   client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
