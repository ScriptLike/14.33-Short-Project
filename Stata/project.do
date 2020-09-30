describe
summarize


/*Regular OLS*/
regress voter_percent educSomeCollege educCollegeUp

outreg2 using regression_results, replace excel dec(3)

regress voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list percentPopulationOver18Male

outreg2 using regression_results, append excel dec(3)

/*start of panel data and fixed regressions*/
xtset id year

/* just state effect */

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list percentPopulationOver18Male, fe vce(cl id)

/* Both state and time effects */

xtreg voter_percent educSomeCollege educCollegeUp i.year, fe vce(cl id)

outreg2 using regression_results, append excel dec(3)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian i.year, fe vce(cl id)

outreg2 using regression_results, append excel dec(3)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list i.year, fe vce(cl id)

outreg2 using regression_results, append excel dec(3)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list percentPopulationOver18Male i.year, fe vce(cl id)

outreg2 using regression_results, append excel dec(3)

