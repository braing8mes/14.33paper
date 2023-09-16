import delimited "C:\Users\Brian Liu\OneDrive - Massachusetts Institute of Technology\Desktop\College classes\14.33\crime_final.csv"

summarize

xtset inegi xmonth

hist crimes
gen lnpop = ln(pop)
hist lnpop

xtreg crime_pc treat i.xmonth, fe robust

xtreg crime_pc treat educ i.xmonth, robust

