---
title: "STDEV.P Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# STDEV.P Function (DAX)
Returns the standard deviation of the entire population.  
  
## Syntax  
  
```  
STDEV.P(<ColumnName>)  
```  
  
#### Parameters  
columnName  
The name of an existing column using standard DAX syntax, usually fully qualified. It cannot be an expression.  
  
## Return Value  
A number representing the standard deviation of the entire population.  
  
## Exceptions  
  
## Remarks  
  
1.  STDEV.P assumes that the column refers to the entire population. If your data represents a sample of the population, then compute the standard deviation by using STDEV.S.  
  
2.  STDEV.P uses the following formula:  
  
    √[∑(x - x̃)²/n]  
  
    where x̃ is the average value of x for the entire population  
  
    and n is the population size  
  
3.  Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
4.  An error is returned if *columnName* contains less than 2 non-blank rows  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example shows the formula for a measure that calculates the standard deviation of the column, SalesAmount_USD, when the table InternetSales_USD is the entire population.  
  
```  
=STDEV.P(InternetSales_USD[SalesAmount_USD])  
```  
