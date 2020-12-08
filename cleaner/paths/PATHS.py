import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = f'{ROOT}/data_to_clean'

DATA_ROOTS = {
    'cases': f'{DATA_PATH}/cases_by_county', 
    'dems': f'{DATA_PATH}/demographics_by_county', 
    'party': f'{DATA_PATH}/politics_by_county',
    'final': f'{DATA_PATH}/final_table'
}
DATA_DIRTY_SRCS = {
    'cases': f'{DATA_ROOTS["cases"]}/cases_by_county.csv',
    'dems': f'{DATA_ROOTS["dems"]}/demographics_by_county.csv',
    'party': f'{DATA_ROOTS["party"]}/political_party_affiliation_by_county.csv'
}
DATA_CLEANER_FNS = {
    'cases': 'clean_cases_by_county.sql',
    'dems': 'clean_dems_by_county.sql',
    'party': 'clean_politics_by_county.sql',
    'final': 'clean_data.sql'
}
DATA_CLEANED_FNS = {
    'cases': 'cleaned_covid_cases_by_county.csv',
    'dems': 'clean_dems_by_county.csv',
    'party': '2016_cleaned_politics_by_county.csv',
    'final': 'clean_data_final.csv'
}
DATA_CLEANED_SRCS = {
    'cases': f'{DATA_ROOTS["cases"]}/{DATA_CLEANED_FNS["cases"]}',
    'dems': f'{DATA_ROOTS["dems"]}/{DATA_CLEANED_FNS["dems"]}',
    'party': f'{DATA_ROOTS["party"]}/{DATA_CLEANED_FNS["party"]}',
    'final': f'{DATA_ROOTS["final"]}/{DATA_CLEANED_FNS["final"]}'
}

