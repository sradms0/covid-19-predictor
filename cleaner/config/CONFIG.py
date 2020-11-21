import os
from paths.PATHS import *

CASES_DIR = DATA_ROOTS["cases"]
DEMS_DIR  = DATA_ROOTS["dems"]
PARTY_DIR = DATA_ROOTS["party"]
FINAL_DIR = DATA_ROOTS["final"]

DIRTY_CASES = DATA_DIRTY_SRCS["cases"] 
DIRTY_DEMS  = DATA_DIRTY_SRCS["dems"]
DIRTY_PARTY = DATA_DIRTY_SRCS["party"] 

CASE_CLEANER_FN = DATA_CLEANER_FNS["cases"]
DEMS_CLEANER_FN = DATA_CLEANER_FNS["dems"]
PARTY_CLEANER_FN = DATA_CLEANER_FNS["party"]
FINAL_CLEANER_FN = DATA_CLEANER_FNS["final"]


CLEANED_CASES_SRC = DATA_CLEANED_SRCS["cases"]
CLEANED_DEMS_SRC = DATA_CLEANED_SRCS["dems"]
CLEANED_PARTY_SRC = DATA_CLEANED_SRCS["party"]
FINAL_SRC = DATA_CLEANED_SRCS["final"]

def clean_and_join_all():
    os.system(f'cd {FINAL_DIR} && sqlite3 < {FINAL_CLEANER_FN}')

def clean_and_copy(cleaner_dir, sql_cleaner, copy_from, copy_to=FINAL_DIR):
    os.system(f'cd {cleaner_dir} && sqlite3 < {sql_cleaner} && cp {copy_from} {copy_to}')

def copy(copy_from, copy_to):
    os.system(f'cp {copy_from} {copy_to}')

