---
description: "Learn more about: VAR.P"
title: "VAR.P function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/13/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# VAR.P

Returns the variance of the entire population.  
  
## Syntax  
  
```dax
VAR.P(<columnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|  columnName  |  The name of an existing column using standard DAX syntax, usually fully qualified. It cannot be an expression.  |  
  
## Return value

A number with the variance of the entire population.  
  
## Remarks  
  
- VAR.P assumes that the column refers the entire population. If your data represents a sample of the population, then compute the variance by using VAR.S.  
  
- VAR.P uses the following formula:  
  
    ∑(x - x̃)<sup>2</sup>/n  
  
    where x̃ is the average value of x for the entire population  
  
    and n is the population size  
  
- Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
- An error is returned if *columnName* contains less than 2 non-blank rows  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example shows the formula for a measure that estimates the variance of the SalesAmount_USD column from the InternetSales_USD table, for the entire population.  
  
```dax
= VAR.P(InternetSales_USD[SalesAmount_USD])  
```
