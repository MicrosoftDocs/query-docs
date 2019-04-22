---
title: "MINX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/19/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MINX

Returns the smallest value that results from evaluating an expression for each row of a table.  

## Syntax

```dax
MINX(<table>, < expression>)  
```
  
#### Parameters
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return value

A smallest value.  
  
## Remarks

The MINX function takes as its first argument a table, or an expression that returns a table. The second argument contains the expression that is evaluated for each row of the table.  
  
Blank values are skipped. TRUE/FALSE values are not supported.
  
## Example 1

The following example filters the table, InternetSales, and returns only rows for a specific sales territory. The formula then finds the minimum value in the column, Freight.  
  
```dax
=MINX( FILTER(InternetSales, [SalesTerritoryKey] = 5),[Freight])  
```
  
## Example 2

The following example uses the same filtered table as in the previous example, but instead of merely looking up values in the column for each row of the filtered table, the function calculates the sum of two columns, Freight and TaxAmt, and returns the smallest value resulting from that calculation.  
  
```dax
=MINX( FILTER(InternetSales, InternetSales[SalesTerritoryKey] = 5), InternetSales[Freight] + InternetSales[TaxAmt])  
```

In the first example, the names of the columns are unqualified. In the second example, the column names are fully qualified.  
  
## See also

[MIN function &#40;DAX&#41;](min-function-dax.md)  
[MINA function &#40;DAX&#41;](mina-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
