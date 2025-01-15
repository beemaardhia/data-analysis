# Dashboard Visualization Project

## Project Structure

```
submission
├───dashboard
|   ├───main_data.csv
|   └───dashboard.py
├───data
|   ├───data_1.csv
|   └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

## Setup Environment - Anaconda

```bash
conda create --name dashboard-env python=3.9
conda activate dashboard-env
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

```bash
mkdir project_dashboard
cd project_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App

Navigate to the `dashboard` directory and run the following command:

```bash
streamlit run dashboard/dashboard.py
```
