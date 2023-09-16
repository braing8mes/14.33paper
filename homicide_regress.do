import delimited "C:\Users\Brian Liu\OneDrive - Massachusetts Institute of Technology\Desktop\College classes\14.33\homicides_final.csv"

summarize

xtset inegi xmonth

xtreg homicides_pc treat i.xmonth, fe robust
estimates store eq1
esttab eq1 using "crime3.tex", se ar2 ///
stats(r2 N) drop (*xmonth) ///
label title(DID regression on homicides per capita) 

eststo: quietly estpost summarize homicides homicides_pc treat pop, listwise

