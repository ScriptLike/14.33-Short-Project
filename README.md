# 14.33 Short Project


PythonDataCleaning
=============

Three folders 
-------------

Data- Contains the raw data from the American Community Survey 5 year estimates, with information about gender,income, and educational attainment. 
In each year folder ex:2012 and 2016 there are three files (renamed) which are the ones used. The other files inside ShortProject/Data/year/ are the raw zip file from the census.gov

ex: 2012_characteristics is the same file in ShortProject/Data/2012Characteristics named ACSDP5Y2012.DP05_data_with_overlays_2020-09-28T003818

ex: 2012_education is the same file in ShortProject/Data/2012Characteristics named ACSDP5Y2012.DP02_data_with_overlays_2020-09-28T0044278

ex: 2012_income is the same file in ShortProject/Data/2012Characteristics named ACSDP5Y2012.DP03_data_with_overlays_2020-09-28T004515

CleanedData- Contains intermediate xlsx files and the final xlsx which is called CleanedData.xlsx produced by the python script.

** CleanedData.xlsx is the excel file you will pass into Stata.

PresidentalReturns- Contains voting data from 2000-2016 at the county level from MIT Elections Lab

Python Script (ExcelDataCleaner)
-------------

To run this script you must change the pathing information to the one that fits your path after you download everything. Afterwards just run the script.

ex: If you see os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\data\\PresidentalReturns\\") 

Change over to the path you stored the folder in


Voting.xlsx
-------------

This is the given voting dataset 


Stata
=============

CleanedData.xlsx
-------------

This is the same excel file from the CleandedData folder use this information as an input to Stata

project.do
-------------

Do file for Stata where the regressions are run