# Project - Numpy

## Team Members

1. Embar, Sai Shiva Hari Prasad
2. Kola, Venkata Seshadri
3. Nuthalapati, Sampath Babu


#### Folder structure

```sh
Repo/
├── CustomFiles			# Code to generate data and figures
├	├── gen-figure.py
├	├── gen_data.py
├	├── gen_data_pre.py
├── coverage        		# Coverage Results 
├── csv_data        		# Auto-generated .csv files
├── figures         		# Auto-generated figures
├── numpy	    		# Numpy 
├── main.py         		# Generates csv_data and figures using CustomFiles
├── .
├── .
├── .
```

## Cloning the Repository

	`git clone {project_url}`

## Requirements for setting up the environment

1. python 3.6 or higher

2. Using virtualenv:

	`python3 -m pip install --user virtualenv`

	`python3 -m venv env`
	
	`source env/bin/activate`

3. `pip install numpy`

4. `pip install pandas`

5. `pip install pydriller`

6. `pip install plotly`

7. `pip install -U kaleido`


## Executing the project
	
	`cd <project folder>`
	 
	`python main.py`
	
## Results
	
	Executing main.py will dynamically generate .csv files (using Pydriller) and figures (using Plotly).

