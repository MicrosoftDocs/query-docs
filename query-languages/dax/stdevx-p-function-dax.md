---
description: "Learn more about: STDEVX.P"
title: "STDEVX.P function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# STDEVX.P

Returns the standard deviation of the entire population.  
  
## Syntax  
  
```dax
STDEVX.P(<table>, <expression>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| table  | Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  |  
|expression   | Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).   |
  
## Return value

A number that represents the standard deviation of the entire population.  
  
## Remarks  
  
- STDEVX.P evaluates *expression* for each row of *table* and returns the standard deviation of expression assuming that table refers to the entire population. If the data in *table* represents a sample of the population, you should compute the standard deviation by using STDEVX.S instead.  
  
- STDEVX.P uses the following formula:  
  
    √[∑(x - x̃)<sup>2</sup>/n]  
  
    where x̃ is the average value of x for the entire population and n is the population size.
  
- Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
- An error is returned if *columnName* contains less than 2 non-blank rows  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example shows the formula for a calculated column that calculates the standard deviation of the unit price per product, when the formula is used in the *Product* table.  
  
```dax
= STDEVX.P(RELATEDTABLE(InternetSales_USD), InternetSales_USD[UnitPrice_USD] – (InternetSales_USD[DiscountAmount_USD]/InternetSales_USD[OrderQuantity]))  
```
