---
title: "VARX.S Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# VARX.S Function (DAX)
Returns the variance of a sample population.  
  
## Syntax  
  
```dax
VARX.S(<table>, <expression>)  
```
  
#### Parameters  
table  
Any DAX expression that returns a table of data.  
  
expression  
Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  
  
## Return Value  
A number that represents the variance of a sample population.  
  
## Exceptions  
  
## Remarks  
  
1.  VARX.S evaluates *expression* for each row of *table* and returns the variance of *expression*; on the assumption that *table* refers to a sample of the population. If *table* represents the entire population, then you should compute the variance by using VARX.P.  
  
2.  VAR.S uses the following formula:  
  
    ∑(x - x̃)²/(n-1)  
  
    where x̃ is the average value of x for the sample population  
  
    and n is the population size  
  
3.  Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
4.  An error is returned if *columnName* contains less than 2 non-blank rows.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example shows the formula for a calculated column that estimates the variance of the unit price per product for a sample population, when the formula is used in the Product table.  
  
```dax
=VARX.S(InternetSales_USD, InternetSales_USD[UnitPrice_USD] – (InternetSales_USD[DiscountAmount_USD]/InternetSales_USD[OrderQuantity]))  
```
