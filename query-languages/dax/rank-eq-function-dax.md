---
title: "RANK.EQ  function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# RANK.EQ
Returns the ranking of a number in a list of numbers.  
  
## Syntax  
  
```dax
RANK.EQ(<value>, <columnName>[, <order>])  
```
  
### Parameters  
value  
Any DAX expression that returns a single scalar value whose rank is to be found. The expression is to be evaluated exactly once, before the function is evaluated, and it’s value passed to the argument list.  
  
columnName  
The name of an existing column against which ranks will be determined. It cannot be an expression or a column created using these functions: ADDCOLUMNS, ROW or SUMMARIZE.  
  
order  
(Optional) A value that specifies how to rank *number*, low to high or high to low:  
  
||||  
|-|-|-|  
|**value**|**alternate value**|**Description**|  
|0 (zero)|FALSE|Ranks in descending order of *columnName*. If *value* is equal to the highest number in *columnName* then **RANK.EQ** is 1.|  
|1|TRUE|Ranks in ascending order of *columnName*. If *value* is equal to the lowest number in *columnName* then **RANK.EQ** is 1.|  
  
## Return value  
A number indicating the rank of *value* among the numbers in *columnName*.  
  
## Exceptions  
  
## Remarks  
  
-   *columnName* cannot refer to any column created using these functions: ADDCOLUMNS, ROW or SUMMARIZE.I  
  
-   If *value* is not in *columnName* or value is a blank, then *RANK.EQ* returns a blank value.  
  
-   Duplicate values of *value* receive the same rank value; the next rank value assigned will be the rank value plus the number of duplicate values. For example if five (5) values are tied with a rank of 11 then the next value will receive a rank of 16 (11 + 5).  
  
## Example  
The following example creates a calculated column that ranks the values in SalesAmount_USD, from the *InternetSales_USD* table, against all numbers in the same column.  
  
```dax
=RANK.EQ(InternetSales_USD[SalesAmount_USD], InternetSales_USD[SalesAmount_USD])  
```
  
## Example  
The following example ranks a subset of values against a given sample. Assume that you have a table of local students with their performance in a specific national test and, also, you have the entire set of scores in that national test. The following calculated column will give you the national ranking for each of the local students.  
  
```dax
=RANK.EQ(Students[Test_Score], NationalScores[Test_Score])  
```
