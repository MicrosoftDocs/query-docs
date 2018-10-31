---
title: "AVERAGE Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# AVERAGE Function (DAX)
Returns the average (arithmetic mean) of all the numbers in a column.  
  
## Syntax  
  
```dax
AVERAGE(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column that contains the numbers for which you want the average.|  
  
## Return Value  
Returns a decimal number that represents the arithmetic mean of the numbers in the column.  
  
## Remarks  
This function takes the specified column as an argument and finds the average of the values in that column. If you want to find the average of an expression that evaluates to a set of numbers, use the AVERAGEX function instead.  
  
Nonnumeric values in the column are handled as follows:  
  
-   If the column contains text, no aggregation can be performed, and the functions returns blanks.  
  
-   If the column contains logical values or empty cells, those values are ignored.  
  
-   Cells with the value zero are included.  
  
-   When you average cells, you must keep in mind the difference between an empty cell and a cell that contains the value 0 (zero). When a cell contains 0, it is added to the sum of numbers and the row is counted among the number of rows used as the divisor. However, when a cell contains a blank, the row is not counted.  
  
Whenever there are no rows to aggregate, the function returns a blank. However, if there are rows, but none of them meet the specified criteria, the function returns 0. Excel also returns a zero if no rows are found that meet the conditions.  
  
## Example  
The following formula returns the average of the values in the column, ExtendedSalesAmount, in the table, InternetSales.  
  
```dax
=AVERAGE(InternetSales[ExtendedSalesAmount])  
```
  
## Related Functions  
The AVERAGEX function can take as its argument an expression that is evaluated for each row in a table. This enables you to perform calculations and then take the average of the calculated values.  
  
The AVERAGEA function takes a column as its argument, but otherwise is like the Excel function of the same name. By using the AVERAGEA function, you can calculate a mean on a column that contains empty values.  
  
## See Also  
[AVERAGEA Function &#40;DAX&#41;](averagea-function-dax.md)  
[AVERAGEX Function &#40;DAX&#41;](averagex-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
