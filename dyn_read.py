########################################################################################################################
# Title: dyn_read.py                                                                                                   #
# Purpose: The goal of this function is to allow a user to read in multiple different file types                       #
#          into dataframes in memory while say looping through a directory. All fields are currently read in           #
#          as strings as reading in strings and then defining types for a prodcution process is best practic           e
#          While Pandas obviously already has read functions, this becomes especially helpful when you need            #
#          to perform operations on files of multiple types.                                                           #
# Last Modified; 11/26/2019                                                                                            #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

def dyn_read(file_path,fwf_layout_path = ""):

    # configure dependencies

    import numpy as np
    import pandas as pd
    import os.path

    # End dependency configuration

    # defining path for cleaner refs below
    path_list = os.path.splitext(file_path)

    # Read in excel files. Current limitation is that first sheet is only read in. But PLEASE don't store your data
    # in excel files.
    if path_list[1][:4] == '.xls':

        # this section shouldn't be too hard to update to read in all sheet names
        ex = pd.ExcelFile(file_path)
        sheets = ex.sheet_names
        df = pd.read_excel(ex)
        df.name = sheets[0]

        return df
    # Read in fixed width files from a layout file. Again, please don't store your data in a fwf. PLEASE use a
    # delimited file. PLEASE.
    elif path_list[1] == '.txt':
        # read in layout file
        # in this example, layout file looks like example below
        '''
        field_name,start,stop
        field_1,0,5
        field_2,5,10
        '''
        fwf_layout = pd.read_csv(fwf_layout_path)
        # build out colspecs for pandas read_fwf colspecs arg
        fwf_layout['colspecs'] = fwf_layout[['start','stop']].values.tolist()
        df = pd.read_fwf(file_path, colspecs=fwf_layout['colspecs'].tolist(), names=fwf_layout['field_name'].to_list(),
                         dtype=str, na_filter=False)

        return df
    # Read in csvs. PLEASE load your data in a delimited format like a csv!!!
    elif path_list[1] == '.csv':
        df = pd.read_csv(file_path, dtype=str)
        return df
    else:
        print("Could not read in the file type passed. Please add this file type into the function")
