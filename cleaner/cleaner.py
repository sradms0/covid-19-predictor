from config.CONFIG import *

def clean_cases():
    clean_and_copy(cleaner_dir=CASES_DIR, sql_cleaner=CASE_CLEANER_FN, copy_from=CLEANED_CASES_SRC)

def clean_dems():
    clean_and_copy(cleaner_dir=DEMS_DIR, sql_cleaner=DEMS_CLEANER_FN, copy_from=CLEANED_DEMS_SRC)

def clean_party():
    copy(copy_from=DIRTY_CASES, copy_to=PARTY_DIR)
    copy(copy_from=DIRTY_CASES, copy_to=FINAL_DIR)
    clean_and_copy(cleaner_dir=PARTY_DIR, sql_cleaner=PARTY_CLEANER_FN, copy_from=CLEANED_PARTY_SRC)

def finalize():
    clean_and_join_all()
