import delimited "C:\Users\Brian Liu\OneDrive - Massachusetts Institute of Technology\Desktop\College classes\14.33\crime_final.csv"

summarize

xtset inegi xmonth

hist crimes
hist crime_pc, width(0.5)
gen lnpop = ln(pop)
hist lnpop

xtreg crime_pc treat i.xmonth, fe robust
estimates store eq1
esttab eq1 using "crime2.tex", se ar2 ///
stats(r2 N) drop (*xmonth) ///
label title(DID regression on crime per capita) 

esttab eq1 using "crime3.tex", cell((coef(fmt(%9.4f)) se(fmt(%9.4f)))) label nobaselevels ///
star(* 0.10 ** 0.05 *** 0.01) stats(r2 N) drop(*xmonth)
xtreg crime_pc treat i.xmonth, robust

esttab eq1 using "crime.tex"

eststo: quietly estpost summarize crimes pop crime_pc treat, listwise
esttab using "summary2.tex", cells("mean sd min max") 
esttab, cells("mean sd min max") nomtitle nonumber
