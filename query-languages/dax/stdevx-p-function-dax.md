---
title: "STDEVX.P Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# STDEVX.P Function (DAX)
Returns the standard deviation of the entire population.  
  
## Syntax  
  
```dax
STDEVX.P(<table>, <expression>)  
```
  
#### Parameters  
*table*  
Any DAX expression that returns a table of data.  
  
*expression*  
Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  
  
## Return Value  
A number that represents the standard deviation of the entire population.  
  
## Remarks  
  
1.  STDEVX.P evaluates *expression* for each row of *table* and returns the standard deviation of expression assuming that table refers to the entire population. If the data in *table* represents a sample of the population, you should compute the standard deviation by using STDEVX.S instead.  
  
2.  STDEVX.P uses the following formula:  
  
    √[∑(x - x̃)²/n]  
  
    where x̃ is the average value of x for the entire population  
  
    and n is the population size  
  
3.  Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
4.  An error is returned if *columnName* contains less than 2 non-blank rows  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [https://go.microsoft.com/fwlink/?LinkId=219171](https://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example shows the formula for a calculated column that calculates the standard deviation of the unit price per product, when the formula is used in the *Product* table.  
  
```dax
=STDEVX.P(RELATEDTABLE(InternetSales_USD), InternetSales_USD[UnitPrice_USD] – (InternetSales_USD[DiscountAmount_USD]/InternetSales_USD[OrderQuantity]))  
```
