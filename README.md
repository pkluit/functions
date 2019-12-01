# Functions

* [Overview](#overview)
* [Index](#index)
* [Descriptions](#descriptions)

## Overview <a name="overview"></a>
The goal of this repo is to store the larger functions that I have created and used personally.I want to keep these seperate from any repos for projects so that I have a central location for some of my favorite functions. Some may be be very general and others might be really specific.

## Index <a name="index"></a>
1. [*dyn_read.py*](#func_1)
2. [*gsheet_to_df.py*](#func_2)

## Descriptions <a name="descriptions"></a>

#### 1. *dyn_read.py* <a name="func_1"></a>
* This function can be passed in a file (currently configured for fwf,csv,and excel) and reads it in and returns it as a pandas dataframe. Pandas already has its own read in functions, but I like this because if I need to loop through a folder of different file types, I can use this to do so and read them all into memory.

#### 2. *gsheet_to_df.py* <a name="func_2"></a>
* This function can be passed in a path to a JSON file and a google sheet workbook name. Ultimately, google sheets is a terrible place to store data. However, as a big chromebook fan, that's where i've choosen to store my running data. This function allows me to pull that data and work with it in pandas
