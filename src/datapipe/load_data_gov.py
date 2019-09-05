import requests
import pandas as pd

# first : get the name
# second : from the name, get the metadata
# third : from the metadata,get the resource id
# finally : use resource_id to get the data

# I/Get the names list
def get_ds_by_index(id, limit=100):
    dataset_names = 'https://data.gov.sg/api/action/package_list'
    r = requests.get(dataset_names)

    print("Getting datasets name lists ...")
    print("Request status : ".upper() + str(r.status_code))

    if(r.status_code == 200):
        names = r.json()['result']

        # II/ Get the resource id
        temp_name = names[id]
        print("Dataset's name  = " + str(temp_name))

        temp_metadata_url = 'https://data.gov.sg/api/action/package_show?id='
        meta_data_url = temp_metadata_url + temp_name

        r = requests.get(meta_data_url)
        
        print("Getting the resource_id of the dataset...")
        print("Request status : ".upper() + str(r.status_code))
        if r.status_code == 200:
            resource_id = r.json()['result']['resources'][0]['id']

            # print(resource_id)

            # III/Get the dataset
            temp_datastore_url = 'https://data.gov.sg/api/action/datastore_search?resource_id='
            datastore_url = temp_datastore_url + resource_id
            datastore_url = datastore_url + "&limit=" + str(limit)

            r = requests.get(datastore_url)
            
            print("Getting the dataset ...")
            print("Request status : ".upper() + str(r.status_code))
            if r.status_code == 200:
                json_str = r.json()

                # Getting the fields inside the dataset
                fields_json = json_str['result']['fields']
                fields = list()
                for item in fields_json:
                    fields.append(item['id'])

                # Getting the records inside the dataset
                records_json = json_str['result']['records']

                dataset = pd.DataFrame(records_json)
                # print(dataset)

                return dataset
            else : print("Data Not Found")
        else : print("Data Not Found")
    else : print("Data Not Found")

# dataset = get_ds_by_index(7, limit=200)
# print(dataset)

def get_ds_list(keywords = [],inner_join=False):
    dataset_names = 'https://data.gov.sg/api/action/package_list'
    r = requests.get(dataset_names)
    print("Getting the dataset names list ... ")
    print("Request status : ".upper() + str(r.status_code))

    if(r.status_code == 200):
        names = r.json()['result']

        names_series = pd.Series(names)
        ds = pd.DataFrame()
        ds.insert(0, "id", names_series.index, True)
        ds.insert(1, "Datasets", names_series, True)

        if(len(keywords) != 0):
            selected_ds = list()
            selected_id = list()
            count_id = 0
            ds_list = ds['Datasets']
            if(not inner_join):
                for ds in ds_list:
                    for key in keywords:
                        if key in ds:
                            selected_ds.append(ds)
                            selected_id.append(count_id)
                            break;
                    count_id += 1
            else: # inner_join = True
                print("Find Datasets with keywords : ".upper() + str(keywords))
                for ds in ds_list:
                    selected = True
                    for key in keywords:
                        if key not in ds:
                            selected = False
                    if(selected):
                        selected_ds.append(ds)
                        selected_id.append(count_id)
                    count_id += 1

            ds = pd.DataFrame()
            ds.insert(0, "id", selected_id, True)
            ds.insert(1, "Datasets", selected_ds, True)
        return ds

def get_link_by_id(id=1097):
    r = requests.get("https://data.gov.sg/api/action/package_list")
    print("Getting the dataset's link ...")
    print("Request status : ".upper() + str(r.status_code))

    if(r.status_code == 200):
        names = r.json()['result']
        dir_link = "https://data.gov.sg/dataset"
        link = dir_link + "/" + names[id]

        return link
    else: return None

ds = get_ds_list(keywords=['sale','flat'], inner_join=True)
print(ds)

# link = get_link_by_id()
# print(link)

# ds = get_ds_by_index(147)
# print(ds)

# PREQUISITES :
    # 1. Install requests - for anaconda : conda install requests
    #    For pip : pip install requests
    # 2. Install pandas - for anaconda : conda install pandas
    #    For pip : pip install pandas
    
# DOCUMENTATION:
# 1. get_ds_by_index(id, limit=100)
    # In this code segment, datasets will be identified using their unique indexes. This function will return a pandas dataset correspond to a given index
    # Firstly, the function will retrieve all dataset names from <package_list> API then assign them with indexes in ascending order
    # Secondly, use the index to get the dataset name then use the name to derive the ""resource_id"" from <package_show> API
    # Finally, use the ""resource_id"" to get the full dataset from <datastore_search> API
    # Note : Some of the datasets may have been removed by data.gov even though they still appear in the names list
    # limit : specifies the number of rows to show

# 2. get_ds_list(keywords = [], inner_join = False)
    # list all the dataset names and their corresponding indexes
    # keywords : a list of searching keywords to help finding among the datasets
    # inner_join : specifies whether datasets must satisfy all keywords or not.

# 3. get_link_by_id(id=1097)
    # gets the link to the data.gov.sg site that has the visualization for the dataset corresponding a specified index
    # the default id is 1097 -> resale-flat-prices suggested by ryzal
    
# MANUAL :
    # copy the file into your working directory
    # then "import load_data_gov" to use the functions in "DOCUMENTATION"
    