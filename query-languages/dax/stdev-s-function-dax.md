---
title: "STDEV.S Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# STDEV.S Function (DAX)
Returns the standard deviation of a sample population.  
  
## Syntax  
  
```  
STDEV.S(<ColumnName>)  
```  
  
#### Parameters  
*columnName*  
The name of an existing column using standard DAX syntax, usually fully qualified. It cannot be an expression.  
  
## Return Value  
A number that represents the standard deviation of a sample population.  
  
## Exceptions  
  
## Remarks  
  
1.  STDEV.S assumes that the column refers to a sample of the population. If your data represents the entire population, then compute the standard deviation by using STDEV.P.  
  
2.  STDEV.S uses the following formula:  
  
    √[∑(x - x̃)²/(n-1)]  
  
    where x̃ is the average value of x for the sample population  
  
    and n is the population size  
  
3.  Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
4.  An error is returned if *columnName* contains less than 2 non-blank rows.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example shows the formula for a measure that calculates the standard deviation of the column, SalesAmount_USD, when the table InternetSales_USD is the sample population.  
  
```  
=STDEV.S(InternetSales_USD[SalesAmount_USD])  
```  
