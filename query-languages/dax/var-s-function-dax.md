---
description: "Learn more about: VAR.S"
title: "VAR.S function (DAX) | Microsoft Docs"
---
# VAR.S

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the variance of a sample population.  
  
## Syntax  
  
```dax
VAR.S(<columnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|`columnName`|  The name of an existing column using standard DAX syntax, usually fully qualified. It cannot be an expression.  |  

## Return value

A number with the variance of a sample population.  
  
## Remarks  
  
- VAR.S assumes that the column refers to a sample of the population. If your data represents the entire population, then compute the variance by using VAR.P.  
  
- VAR.S uses the following formula:  
  
    ∑(x - x̃)<sup>2</sup>/(n-1)  
  
    where x̃ is the average value of x for the sample population  
  
    and n is the population size  
  
- Blank rows are filtered out from `columnName` and not considered in the calculations.  
  
- An error is returned if `columnName` contains less than 2 non-blank rows.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example shows the formula for a measure that calculates the variance of the SalesAmount_USD column from the InternetSales_USD for a sample population.  
  
```dax
= VAR.S(InternetSales_USD[SalesAmount_USD])  
```
