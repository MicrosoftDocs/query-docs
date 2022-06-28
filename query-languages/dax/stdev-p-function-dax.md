---
description: "Learn more about: STDEV.P"
title: "STDEV.P function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# STDEV.P

Returns the standard deviation of the entire population.  
  
## Syntax  
  
```dax
STDEV.P(<ColumnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| columnName | The name of an existing column using standard DAX syntax, usually fully qualified. It cannot be an expression.   |  
  
## Return value

A number representing the standard deviation of the entire population.   
  
## Remarks  
  
- STDEV.P assumes that the column refers to the entire population. If your data represents a sample of the population, then compute the standard deviation by using STDEV.S.  
  
- STDEV.P uses the following formula:  
  
    √[∑(x - x̃)<sup>2</sup>/n]  
  
    where x̃ is the average value of x for the entire population and n is the population size.
  
- Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
- An error is returned if *columnName* contains less than 2 non-blank rows  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example shows the formula for a measure that calculates the standard deviation of the column, SalesAmount_USD, when the table InternetSales_USD is the entire population.  
  
```dax
= STDEV.P(InternetSales_USD[SalesAmount_USD])  
```
