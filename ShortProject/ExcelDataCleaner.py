import pandas as pd
import os
import math
import numpy as np

def create_template():
	'''
	Create the dataframe template that I will use to merge all datasets
	'''	
	voting_data = pd.read_excel('Voting.xlsx', header = 0)
	FIPS_Values = voting_data.iloc[:, 0].tolist()
	FIPS_set = set(FIPS_Values)
	##Get the first three columns of the voting dataset as a base
	template_data = voting_data.iloc[: , 0:4]
	renamed_template = template_data.rename({'FIPS':'id', 'stateFIPS':'stateFIPS', 'state':'state','county':'county'}, axis='columns')
	return renamed_template

def create_presidential_dict(year):
	'''
	Create the dict to store presidental data
	'''	
	os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\data\\PresidentalReturns\\") 
	presidental_data = pd.read_excel('countypres_2000-2016.xlsx', header = 0)
	##get only this years data
	year = int(year)
	year_rows = presidental_data.loc[presidental_data['year'] == year]
	id_tag = 'FIPS'
	total_votes_tag = "totalvotes"

	seen_fips_set = set()
	id_values = []
	total_votes = []

	for row in year_rows.itertuples():
		id_value = getattr(row, id_tag)
		if not np.isnan(id_value):
			id_value=int(id_value)
		else:
			continue
		total_vote = getattr(row, total_votes_tag)
		if not np.isnan(total_vote):
			total_vote=total_vote
		else:
			continue

		if id_value not in seen_fips_set:
			seen_fips_set.add(id_value)
			id_values.append(id_value)
			total_votes.append(total_vote)
		else:
			continue
		
	dictionary_votes = {}
	dictionary_votes['id'] = id_values
	dictionary_votes['total_votes'] = total_votes
	return dictionary_votes





def create_income_dict(year):
	'''
	In this excel sheet we want the median house hold income so we take the id and the median house hold index as a dictionary to store as a python dataframe later
	'''

	os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\data\\"+year+"\\") 
	income = pd.read_excel(year+'_income.xlsx', header = 0)
	id_list = []
	median_income_list = []

	id_tag = 'GEO_ID'
	medianIncome_tag = 'DP03_0062E'
	counter = 0
	for row in income.itertuples():
		##skip first row
		if counter == 0:
			counter = 1
			continue
		unparesd_id_value = getattr(row, id_tag)
		id_value = int(unparesd_id_value[9:])
		median_house_income = getattr(row,medianIncome_tag)
		id_list.append(id_value)
		median_income_list.append(median_house_income)

	dictionary_income = {}
	dictionary_income['id'] = id_list
	dictionary_income['median_income_list'] = median_income_list

	return dictionary_income


def create_education_dict(year):
	'''
	In this function we take the necessary infomration such as educTillHs,educSomeCollege, and educCollegeUp from the proper excel file to a python dictionary to turn into a data
	frame later
	'''

	os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\data\\"+year+"\\") 
	education = pd.read_excel(year+'_education.xlsx', header = 0)

	id_list = []
	educTillHS = []
	educSomeCollege = []
	educCollegeUp = []

	id_tag = 'GEO_ID'
	less_than_9th_tag = 'DP02_0059PE'
	value_9th_to_12th_tag = 'DP02_0060PE'
	higschool_grad_tag = 'DP02_0061PE'
	college_up_tag = 'DP02_0067PE'

	counter = 0
	for row in education.itertuples():
		##skip first row
		if counter == 0:
			counter = 1
			continue
		unparesd_id_value = getattr(row, id_tag)
		id_value = int(unparesd_id_value[9:])

		less_than_9th = getattr(row, less_than_9th_tag) 
		value_9th_to_12th = getattr(row, value_9th_to_12th_tag) 
		higschool_grad = getattr(row, higschool_grad_tag) 

		TillHS = less_than_9th+value_9th_to_12th+higschool_grad
		CollegeUp = getattr(row, college_up_tag) 
		SomeCollege = 100-TillHS-CollegeUp

		id_list.append(id_value)
		educTillHS.append(TillHS)
		educSomeCollege.append(SomeCollege)
		educCollegeUp.append(CollegeUp)

	dictionary_education= {}
	dictionary_education['id'] = id_list
	dictionary_education['educTillHS'] = educTillHS
	dictionary_education['educSomeCollege'] = educSomeCollege
	dictionary_education['educCollegeUp'] = educCollegeUp

	return dictionary_education

def create_characteristics_dict(year):
	'''
	A function to gather the needed characteristics such as total pop and race information for the project returns a dictionary
	'''

	os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\data\\"+year+"\\") 
	characteristics = pd.read_excel(year+'_characteristics.xlsx', header = 0)

	id_list = []
	total_pop_18 = []
	total_male_pop_18 = []
	total_female_pop_18 = []
	black = []
	white = []
	asian = []
	other = []

	id_tag = 'GEO_ID'
	total_pop_18_years_and_older_tag = 'DP05_0018E'
	estimate_male_18_years_and_older_tag = 'DP05_0023PE'
	estimate_female_18_years_and_older_tag = 'DP05_0024PE'
	share_black_tag = 'DP05_0033PE'
	share_white_tag = 'DP05_0032PE'
	share_asian_tag = 'DP05_0039PE'
	

	counter = 0
	for row in characteristics.itertuples():
		##skip first row
		if counter == 0:
			counter = 1
			continue
		unparesd_id_value = getattr(row, id_tag)
		id_value = int(unparesd_id_value[9:])

		total_pop_18_years_and_older = getattr(row, total_pop_18_years_and_older_tag) 
		estimate_male_18_years_and_older = getattr(row, estimate_male_18_years_and_older_tag) 
		estimate_female_18_years_and_older = getattr(row, estimate_female_18_years_and_older_tag)
		share_black = getattr(row,share_black_tag)
		share_white = getattr(row,share_white_tag)
		share_asian = getattr(row,share_asian_tag)
		share_other = 100-share_black-share_white-share_asian

		id_list.append(id_value)
		total_pop_18.append(total_pop_18_years_and_older)
		total_male_pop_18.append(estimate_male_18_years_and_older)
		total_female_pop_18.append(estimate_female_18_years_and_older)
		black.append(share_black)
		white.append(share_white) 
		asian.append(share_asian)
		other.append(share_other)

	dictionary_characteristic= {}
	dictionary_characteristic['id'] = id_list
	dictionary_characteristic['populationOver18'] = total_pop_18
	dictionary_characteristic['percentPopulationOver18Male'] = total_male_pop_18
	dictionary_characteristic['percentPopulationOver18FeMale'] = total_female_pop_18
	dictionary_characteristic['shareBlack'] = black
	dictionary_characteristic['shareWhite'] = white
	dictionary_characteristic['shareAsian'] = asian
	dictionary_characteristic['shareOtherRace'] = other


	return dictionary_characteristic


def combine_data():

	'''
	Combine all previous python dictionary into a dataframe to export to excel
	'''

	list_years = ["2012","2016"]

	for year in list_years:

		os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\") 

		df_template = create_template()

		

		char_dic = pd.DataFrame.from_dict(create_characteristics_dict(year))
		educ_dic = pd.DataFrame.from_dict(create_education_dict(year))
		income_dic = pd.DataFrame.from_dict(create_income_dict(year))
		vote_dic = pd.DataFrame.from_dict(create_presidential_dict(year))

		

		df_template = pd.merge(df_template, char_dic, on='id')
		df_template = pd.merge(df_template, educ_dic, on='id')
		df_template = pd.merge(df_template, income_dic, on='id')
		df_template = pd.merge(df_template, vote_dic, on='id')


		os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\CleanedData\\") 

		df_template.to_excel(year+"_output.xlsx",index=False)  



def populate_with_year_and_turnout_percentage():
	'''
	Takes the completed data and adds the voter turnout 
	'''
	os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\CleanedData\\") 
	list_years = ["2012","2016"]

	years = []
	turnont_percentage = []
	id_values = []

	populationOver18_tag= "populationOver18"
	total_votes_tag="total_votes"
	id_tag ="id"


	for year in list_years:
		current_file = pd.read_excel(year+"_output.xlsx", header = 0)
		for row in current_file.itertuples():
			id_value = getattr(row,id_tag)
			total_pop = getattr(row,populationOver18_tag)
			voter_num = getattr(row,total_votes_tag)

			id_values.append(id_value)
			turnont_percentage.append((voter_num/total_pop)*100)
			years.append(year)


		dictionary_result= {}
		dictionary_result['id'] = id_values
		dictionary_result['voter_percent'] = turnont_percentage
		dictionary_result['year'] = years


		extra_data = pd.DataFrame.from_dict(dictionary_result)

		current_file = pd.merge(current_file, extra_data, on='id')

		os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\CleanedData\\") 

		current_file.to_excel(year+"_final_output.xlsx",index=False)  

		years = []
		turnont_percentage = []
		id_values = []


def combine_excel_sheets():
	'''
	Combine to form the panel data
	'''
	os.chdir(r"C:\\Users\\larry\\Dropbox (MIT)\\Main\\MIT 2020\\14.33\\PythonDataCleaning\\CleanedData\\") 

	year_2012 = pd.read_excel("2012"+"_final_output.xlsx", header = 0)
	year_2016 = pd.read_excel("2016"+"_final_output.xlsx", header = 0)


	result = year_2012.append(year_2016)
	result.to_excel("CleanedData.xlsx",index=False)  

			
def run_all():
	'''
	Main function run this to run everything
	'''
	combine_data()
	populate_with_year_and_turnout_percentage()
	combine_excel_sheets()

run_all()







  