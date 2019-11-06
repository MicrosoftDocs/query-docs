---
title: "Statistical functions (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/22/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# Statistical functions

Data Analysis Expressions (DAX) provides many functions for creating aggregations such as sums, counts, and averages. These functions are very similar to aggregation functions used by Microsoft Excel. This section lists the statistical and aggregation functions provided in DAX.  
  
## In this category

|Function  |Description  |
|---------|---------|
|[ADDCOLUMNS](addcolumns-function-dax.md)      | Adds calculated columns to the given table or table expression.          |
|[APPROXIMATEDISTINCTCOUNT](approximate-distinctcount-function-dax.md)     |   Returns the *approximate* number of rows that contain distinct values in a column.      |
|[AVERAGE](average-function-dax.md)     |   Returns the average (arithmetic mean) of all the numbers in a column.       |
|[AVERAGEA](averagea-function-dax.md)     | Returns the average (arithmetic mean) of the values in a column.         |
|[AVERAGEX](averagex-function-dax.md)    | Calculates the average (arithmetic mean) of a set of expressions evaluated over a table.          |
|[BETA.DIST](beta-dist-function-dax.md)     |  Returns the beta distribution.        |
|[BETA.INV](beta-inv-function-dax.md)     |  Returns the inverse of the beta cumulative probability density function (BETA.DIST).         |
|[CHISQ.INV](chisq-inv-function-dax.md)     |  Returns the inverse of the left-tailed probability of the chi-squared distribution.         |
|[CHISQ.INV.RT](chisq-inv-rt-function-dax.md)      |  Returns the inverse of the right-tailed probability of the chi-squared distribution.       |
|[CONFIDENCE.NORM](confidence-norm-function-dax.md)      | The confidence interval is a range of values.         |
|[CONFIDENCE.T](confidence-t-function-dax.md)      |  Returns the confidence interval for a population mean, using a Student's t distribution.       |
|[COUNT](count-function-dax.md)      |  The COUNT function counts the number of cells in a column that contain numbers.       |
|[COUNTA](counta-function-dax.md)     |  The COUNTA function counts the number of cells in a column that are not empty.       |
|[COUNTAX](countax-function-dax.md)     |  The COUNTAX function counts nonblank results when evaluating the result of an expression over a table.        |
|[COUNTBLANK](countblank-function-dax.md)     |  Counts the number of blank cells in a column.        |
|[COUNTROWS](countrows-function-dax.md)      |  The COUNTROWS function counts the number of rows in the specified table, or in a table defined by an expression.        |
|[COUNTX](countx-function-dax.md)       |  Counts the number of rows that contain a number or an expression that evaluates to a number, when evaluating an expression over a table.         |
|[CROSSJOIN ](crossjoin-function-dax.md)      |  Returns a table that contains the Cartesian product of all rows from all tables in the arguments.      |
|[DATATABLE](datatable-function.md)      |  Provides a mechanism for declaring an inline set of data values.       |
|[DISTINCTCOUNT](distinctcount-function-dax.md)     |  Counts the number of distinct values in a column.         |
|[DISTINCTCOUNTNOBLANK](distinctcountnoblank-function-dax.md)    |   Counts the number of distinct values in a column.      |
|[EXPON.DIST](expon-dist-function-dax.md)      |  Returns the exponential distribution.        |
|[GENERATE ](generate-function-dax.md)      |  Returns a table with the Cartesian product between each row in *table1* and the table that results from evaluating *table2* in the context of the current row from *table1*.       |
|[GENERATEALL](generateall-function-dax.md)     |  Returns a table with the Cartesian product between each row in *table1* and the table that results from evaluating *table2* in the context of the current row from *table1*.         |
|[GEOMEAN](geomean-function-dax.md)     |  Returns the geometric mean of the numbers in a column.        |
|[GEOMEANX](geomeanx-function-dax.md)      | Returns the geometric mean of an expression evaluated for each row in a table.        |
|[MAX](max-function-dax.md)    |  Returns the largest numeric value in a column, or between two scalar expressions.        |
|[MAXA](maxa-function-dax.md)     |  Returns the largest value in a column.       |
|[MAXX](maxx-function-dax.md)       |  Evaluates an expression for each row of a table and returns the largest numeric value.        |
|[MEDIAN](median-function-dax.md)     |  Returns the median of numbers in a column.       |
|[MEDIANX](medianx-function-dax.md)     |   Returns the median number of an expression evaluated for each row in a table.       |
|[MIN](min-function-dax.md)     |  Returns the smallest numeric value in a column, or between two scalar expressions.       |
|[MINA](mina-function-dax.md)      | Returns the smallest value in a column, including any logical values and numbers represented as text.          |
|[MINX](minx-function-dax.md)      |  Returns the smallest numeric value that results from evaluating an expression for each row of a table.        |
|[NORM.DIST](norm-dist-dax.md)     |  Returns the normal distribution for the specified mean and standard deviation.        |
|[NORM.INV](norm-inv-dax.md)       |  The inverse of the normal cumulative distribution for the specified mean and standard deviation.       |
|[NORM.S.DIST](norm-s-dist-dax.md)       |  Returns the standard normal distribution (has a mean of zero and a standard deviation of one).       |
|[NORM.S.INV](norm-s-inv-dax.md)     |  Returns the inverse of the standard normal cumulative distribution.       |
|[PERCENTILE.EXC](percentile-exc-function-dax.md)     |  Returns the k-th percentile of values in a range, where k is in the range 0..1, exclusive.        |
|[PERCENTILE.INC](percentile-inc-function-dax.md)      |  Returns the k-th percentile of values in a range, where k is in the range 0..1, inclusive.        |
|[PERCENTILEX.EXC](percentilex-exc-function-dax.md)     | Returns the percentile number of an expression evaluated for each row in a table.        |
|[PERCENTILEX.INC](percentilex-inc-function-dax.md)    | Returns the percentile number of an expression evaluated for each row in a table.         |
|[POISSON.DIST](poisson-dist-function-dax.md)      |  Returns the Poisson distribution.       |
|[RANK.EQ ](rank-eq-function-dax.md)    | Returns the ranking of a number in a list of numbers.        |
|[RANKX](rankx-function-dax.md)      | Returns the ranking of a number in a list of numbers for each row in the *table* argument.          |
|[ROW](row-function-dax.md)     |  Returns a table with a single row containing values that result from the expressions given to each column.         |
|[SAMPLE](sample-function-dax.md)       |  Returns a sample of N rows from the specified table.        |
|[SELECTCOLUMNS](selectcolumns-function-dax.md)    |  Adds calculated columns to the given table or table expression.         |
|[SIN](sin-function-dax.md)     | Returns the sine of the given angle.          |
|[SINH](sinh-function-dax.md)       | Returns the hyperbolic sine of a number.          |
|[STDEV.P](stdev-p-function-dax.md)     |  Returns the standard deviation of the entire population.        |
|[STDEV.S](stdev-s-function-dax.md)      |  Returns the standard deviation of a sample population.        |
|[STDEVX.P](stdevx-p-function-dax.md)      | Returns the standard deviation of the entire population.         |
|[STDEVX.S](stdevx-s-function-dax.md)      |  Returns the standard deviation of a sample population.         |
|[SQRTPI](sqrtpi-function-dax.md)     |  Returns the square root of (number * pi).       |
|[SUMMARIZE](summarize-function-dax.md)      | Returns a summary table for the requested totals over a set of groups.          |
|[T.DIST](t-dist-dax.md)    | Returns the Student's left-tailed t-distribution.        |
|[T.DIST.2T](t-dist-2t-dax.md)    | Returns the two-tailed Student's t-distribution.        |
|[T.DIST.RT](t-dist-rt-dax.md)     | Returns the right-tailed Student's t-distribution.        |
|[T.INV](t-inv-dax.md)     | Returns the left-tailed inverse of the Student's t-distribution.        |
|[T.INV.2t](t-inv-2t-dax.md)     | Returns the two-tailed inverse of the Student's t-distribution.        |
|[TAN](tan-function-dax.md)      |  Returns the tangent of the given angle.         |
|[TANH](tanh-function-dax.md)     |  Returns the hyperbolic tangent of a number.        |
|[TOPN](topn-function-dax.md)     |  Returns the top N rows of the specified table.       |
|[VAR.P](var-p-function-dax.md)    | Returns the variance of the entire population.         |
|[VAR.S](var-s-function-dax.md)    |  Returns the variance of a sample population.         |
|[VARX.P](varx-p-function-dax.md)     | Returns the variance of the entire population.         |
|[VARX.S](varx-s-function-dax.md)     | Returns the variance of a sample population.        |
|[XIRR](xirr-function-dax.md)     |  Returns the internal rate of return for a schedule of cash flows that is not necessarily periodic.       |
|[XNPV](xnpv-function-dax.md)      |  Returns the present value for a schedule of cash flows that is not necessarily periodic.       |
