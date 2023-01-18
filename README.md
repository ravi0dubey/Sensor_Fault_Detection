# neurolab-mongo-python



### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### Step 3 - Download datafile

```bash
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```


### Step 4 - Connect to Mongodb

```bash
Click on new connection and enter url mongodb://localhost:27017/neurolabDB. This will connect to mongodb
```


### Step 5 - Create data_Dump.py file to upload datafile into mongdb
```bash
python data_dump.py
```

### Step 6 - perform git activity in neurolab

```bash
git activity 
```