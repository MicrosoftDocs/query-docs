---
title: "MAXX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/19/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MAXX

Evaluates an expression for each row of a table and returns the largest value.  
  
## Syntax  
  
```dax
MAXX(<table>,<expression>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return value

The largest value.
  
## Remarks

The **table** argument to the MAXX function can be a table name, or an expression that evaluates to a table. The second argument indicates the expression to be evaluated for each row of the table.  
  
Of the values to evaluate, only the following are counted:  
  
- Numbers

- Texts
  
- Dates
  
Blank values are skipped. TRUE/FALSE values are not supported.
  
## Example 1

The following formula uses an expression as the second argument to calculate the total amount of taxes and shipping for each order in the table, InternetSales. The expected result is 375.7184.  
  
```dax
=MAXX(InternetSales, InternetSales[TaxAmt]+ InternetSales[Freight])  
```
  
## Example 2

The following formula first filters the table InternetSales, by using a FILTER expression, to return a subset of orders for a specific sales region, defined as [SalesTerritory] = 5. The MAXX function then evaluates the expression used as the second argument for each row of the filtered table, and returns the highest amount for taxes and shipping for just those orders. The expected result is 250.3724.  
  
```dax
=MAXX(FILTER(InternetSales,[SalesTerritoryCode]="5"), InternetSales[TaxAmt]+ InternetSales[Freight])  
```
  
## See also

[MAX function &#40;DAX&#41;](max-function-dax.md)  
[MAXA function &#40;DAX&#41;](maxa-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
