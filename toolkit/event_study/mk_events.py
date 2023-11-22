""" mk_events.py

Utilities to create events from recommendations
"""
import pandas as pd

import event_study.config as cfg


#   Functions to process recommendations into events
def mk_event_df(tic):
    """ Subsets and processes recommendations given a ticker and return a data
    frame with all events in the sample.

    Parameters
    ----------
    tic : str
        Ticker

    Returns
    -------
    pandas dataframe

        The columns are:
        * event_date : string
            Date string with format 'YYYY-MM-DD'
        * firm : string
            Name of the firm (upper case)
        * event_type : string
            Either "downgrade" or "upgrade"

        index: integer
            Index named 'event_id' starting at 1

    Notes
    -----
    This function will perform the following actions:

    1. Read the appropriate CSV file with recommendations into a data frame
    2. Create variables identifying the firm and the event date
    3. Deal with multiple recommendations
    4. Create a table with all relevant events

    """


if __name__ == "__main__":
    tic = 'TSLA'
    df = mk_event_df(tic)
    print(df)
    df.info()