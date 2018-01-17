---
title: "MAXX Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.MAXX.f1"
helpviewer_keywords: 
  - "Maximum value, MAXX"
  - "MAXX function"
ms.assetid: 85e12579-8162-4aab-88a4-e1fb485b59c6
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# MAXX Function (DAX)
Evaluates an expression for each row of a table and returns the largest numeric value.  
  
## Syntax  
  
```  
MAXX(<table>,<expression>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**table**|The table containing the rows for which the expression will be evaluated.|  
|**expression**|The expression to be evaluated for each row of the table.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The **table** argument to the MAXX function can be a table name, or an expression that evaluates to a table. The second argument indicates the expression to be evaluated for each row of the table.  
  
Of the values to evaluate, only the following are counted:  
  
-   Numbers. If the expression does not evaluate to a number, MAXX returns 0 (zero).  
  
-   Dates.  
  
Empty cells, logical values, and text values are ignored. If you want to include non-numeric values in the formula, use the MAXA function.  
  
If a blank cell is included in the column or expression, MAXX returns an empty column.  
  
## Example  
The following formula uses an expression as the second argument to calculate the total amount of taxes and shipping for each order in the table, InternetSales. The expected result is 375.7184.  
  
```  
=MAXX(InternetSales, InternetSales[TaxAmt]+ InternetSales[Freight])  
```  
  
## Example  
The following formula first filters the table InternetSales, by using a FILTER expression, to return a subset of orders for a specific sales region, defined as [SalesTerritory] = 5. The MAXX function then evaluates the expression used as the second argument for each row of the filtered table, and returns the highest amount for taxes and shipping for just those orders. The expected result is 250.3724.  
  
```  
=MAXX(FILTER(InternetSales,[SalesTerritoryCode]="5"), InternetSales[TaxAmt]+ InternetSales[Freight])  
```  
  
## See Also  
[MAX Function &#40;DAX&#41;](../DAX/max-function-dax.md)  
[MAXA Function &#40;DAX&#41;](../DAX/maxa-function-dax.md)  
[MAXX Function &#40;DAX&#41;](../DAX/maxx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](../DAX/statistical-functions-dax.md)  
  
