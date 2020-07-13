---
title: "VARX.P function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/13/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# VARX.P

Returns the variance of the entire population.  
  
## Syntax  
  
```dax
VARX.P(<table>, <expression>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|  table|  Any DAX expression that returns a table of data. |  
| expression |  Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  |
  
## Return value

A number with the variance of the entire population.  
  
## Remarks  
  
- VARX.P evaluates &lt;expression&gt; for each row of &lt;table&gt; and returns the variance of &lt;expression&gt; assuming that &lt;table&gt; refers to the entire population.. If &lt;table&gt; represents a sample of the population, then compute the variance by using VARX.S.  
  
- VARX.P uses the following formula:  
  
    ∑(x - x̃)<sup>2</sup>/n  
  
    where x̃ is the average value of x for the entire population  
  
    and n is the population size  
  
- Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
- An error is returned if *columnName* contains less than 2 non-blank rows  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example shows the formula for a calculated column that calculates the variance of the unit price per product, when the formula is used in the Product table  
  
```dax
= VARX.P(InternetSales_USD, InternetSales_USD[UnitPrice_USD] –(InternetSales_USD[DiscountAmount_USD]/InternetSales_USD[OrderQuantity]))  
```
