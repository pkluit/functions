########################################################################################################################
# Title: gsheet_to_df.py                                                                                               #
# Purpose: The goal of this function is to allow a user to read in a google sheet and convert its data to a pandas df  #
# Last Modified; 12/1/2019                                                                                             #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################


def gsheet_to_df(svc_acct_path,wb_name):

    # Begin Import Dependencies
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import pandas as pd
    # End Import Dependencies

    # Set scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Build credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name(svc_acct_path, scope)

    # Build client with
    client = gspread.authorize(creds)

    # API request
    data = (client.open(wb_name).sheet1).get_all_values()

    # Convert data to Pandas Dataframe
    df = pd.DataFrame(data[1:],columns=data[0])

    return df


