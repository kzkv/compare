"""
1. Reads from two files `transactors.xls` and `vars.xls`; both have to be `xls`, not `xlsx`.
2. Grabs first columns from both files.
3. Makes sure records are unique.
"""

import pandas
import numpy

# iloc[:, 0] gets first column; lowercase; get unique
trts = pandas.read_excel("transactors.xls").iloc[:, 0].str.lower().unique()
vars = pandas.read_excel("vars.xls").iloc[:, 0].str.lower().unique()

intersection = numpy.intersect1d(trts, vars)

lt = len(trts)
lv = len(vars)
li = len(intersection)

print("Unique rows")
print(f"transactors: {lt}")
print(f"vars: {lv}")
print("")
print(f"Intersection (common rows): {li}")
print("")
print("Fractions ")
print(f"transactors: {(li / lt) * 100:.1f}% common")
print(f"vars: {(li / lv) * 100:.1f}% common")
