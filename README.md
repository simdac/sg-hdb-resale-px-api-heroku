<p align="center"><a href="http://simdaclub.com/">
  <img width="350" height="350"  src="https://i.imgur.com/OS0Eood.png"></a>
</p>

# [`SIM DAC`](http://simdaclub.com/): SG HDB Resale Price App

This repository is dedicated for SIM DAC's end-to-end implementation of a dashboard application for the use case of Singapore's HDB resale price prediction. This project is part of a tryout for SIM DAC's mentorship initiative.

# Overview of Application
> Coming soon...

# Project Structure
> Coming soon...

# Contributions
For a set of basic guidelines on how to contribute to this project, please refer to [`CONTRIBUTING.md`](./CONTRIBUTING.md).

> More coming soon...

# Code of Conduct
This project and everyone participating in it is governed by the this project's ['Code of Conduct'](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [ryzalkamis@gmail.com](mailto:ryzalkamis@gmail.com).

# Credits
> Coming soon...
Nong Minh Hieu
Hello it's Hieu ahihihi

Hello guys, the DE team has completed developing the data pipeline to load the datasets from the API of data.gov.sg to pandas DataFrame. 
All The functions required to load data from the API to DataFrames are included in 'load_data_gov.py' file under src/pipeline folder.
If you want to see the demonstration of how the functions work, please refer to my 'load_data_gov.ipynb' file under notebooks folder.
# Note :
For all the functions in 'load_data_gov.py' to work, you need the internet. However, if you are working offline, I have provided a sqlite
database file. you can get it by downloading the zip file : 'ryzal.zip', unzip it and go to database folder. You will see a .db file
called 'data.db' inside the ryzal folder.

# Documentation for 'load_data_gov.py':
PREQUISITES :
1. Install requests - for anaconda : conda install requests
                      for pip : pip install requests
2. Install pandas - for anaconda : conda install pandas
                    for pip : pip install pandas

DOCUMENTATION:
1. get_ds_by_index(id, limit=100)
    In this code segment, datasets will be identified using their unique indexes. This function will return a pandas dataset correspond to a given index
    Firstly, the function will retrieve all dataset names from <package_list> API then assign them with indexes in ascending order
    Secondly, use the index to get the dataset name then use the name to derive the ""resource_id"" from <package_show> API
    Finally, use the ""resource_id"" to get the full dataset from <datastore_search> API
    Note : Some of the datasets may have been removed by data.gov even though they still appear in the names list
    limit : specifies the number of rows to show

2. get_ds_list(keywords = [], inner_join = False)
    list all the dataset names and their corresponding indexes
    keywords : a list of searching keywords to help finding among the datasets
    inner_join : specifies whether datasets must satisfy all keywords or not.

3. get_link_by_id(id=1097)
    gets the link to the data.gov.sg site that has the visualization for the dataset corresponding a specified index
    the default id is 1097 -> resale-flat-prices suggested by ryzal

4. describe_ds(id)
    providing the id of the dataset, the function describe_id will return a pandas dataset that have
    the names of the columns and the types of those columns in the dataset.

5. ds_to_csv(id, dir_path, limit=100)
    for a given dataset id, this function exports the dataset to the specified directory path
    dir_path : specifies the directory to which the dataset is exported
    id : the dataset's id
    limit : the number of rows to be exported, the default is 100

MANUAL :
    copy the file into your working directory
    then "import load_data_gov" to use the functions in "DOCUMENTATION"
