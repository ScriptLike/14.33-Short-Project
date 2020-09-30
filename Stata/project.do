describe
summarize

/*Regular OLS*/
regress voter_percent educSomeCollege educCollegeUp

regress voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list percentPopulationOver18Male


/*start of panel data and fixed regressions*/
xtset id year

/* Start of only time effect (constant through time) different per county*/
xtreg voter_percent educSomeCollege educCollegeUp i.year, vce(cl id)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian i.year, vce(cl id)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list i.year, vce(cl id)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list percentPopulationOver18Male i.year, vce(cl id)

/* Start of only fixed effect per county different through time (state effect)*/
xtreg voter_percent educSomeCollege educCollegeUp, fe vce(cl id)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian, fe vce(cl id)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list, fe vce(cl id)

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list percentPopulationOver18Male, fe vce(cl id)

/* Both state and time effects */

xtreg voter_percent educSomeCollege educCollegeUp shareBlack shareWhite shareAsian median_income_list percentPopulationOver18Male i.year, fe vce(cl id)

