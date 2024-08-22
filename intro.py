from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numerapi



#instance of numerai
napi = numerapi.NumerAPI()

#LIST ALL DATASETS
dataset = napi.list_datasets()
print(dataset)
for data in dataset:
    print(data)
    
#getting the currrent round of tournament
current_round = napi.get_current_round()

#download files with format of parque and if they are int8
for file in dataset:
    if "parque" in file and "int8" in file:
        if "training" in file and "validation" in file and "V4" in file:
            #save them
            napi.download_dataset(file,f"Data/{file}")
            #napi.download_latest_data("training","parquet","Data")
        else:
            Path(f"Data/{current_round}").mkdir(parents=False, exist_ok=True)
            napi.download_dataset(file,"Data/{current_round}/{file}")


df = pd.read_parquet("Data/latest_numerai_training_data.parquet")
print(df.shape)




