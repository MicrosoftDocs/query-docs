---
title: "MINX Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MINX Function (DAX)
Returns the smallest numeric value that results from evaluating an expression for each row of a table.  
  
## Syntax  
  
```  
MINX(<table>, < expression>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**table**|The table containing the rows for which the expression will be evaluated.|  
|**expression**|The expression to be evaluated for each row of the table.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The MINX function takes as its first argument a table, or an expression that returns a table. The second argument contains the expression that is evaluated for each row of the table.  
  
The MINX function evaluates the results of the expression in the second argument according to the following rules:  
  
-   Only numbers are counted. If the expression does not result in a number, MINX returns 0 (zero).  
  
-   Empty cells, logical values, and text values are ignored. Numbers represented as text are treated as text.  
  
If you want to include logical values and text representations of numbers in a reference as part of the calculation, use the MINA function.  
  
## Example  
The following example filters the table, InternetSales, and returns only rows for a specific sales territory. The formula then finds the minimum value in the column, Freight.  
  
```  
=MINX( FILTER(InternetSales, [SalesTerritoryKey] = 5),[Freight])  
```  
  
## Example  
The following example uses the same filtered table as in the previous example, but instead of merely looking up values in the column for each row of the filtered table, the function calculates the sum of two columns, Freight and TaxAmt, and returns the smallest value resulting from that calculation.  
  
```  
=MINX( FILTER(InternetSales, InternetSales[SalesTerritoryKey] = 5), InternetSales[Freight] + InternetSales[TaxAmt])  
```  
  
## Comments  
In the first example, the names of the columns are unqualified. In the second example, the column names are fully qualified.  
  
## See Also  
[MIN Function &#40;DAX&#41;](min-function-dax.md)  
[MINA Function &#40;DAX&#41;](mina-function-dax.md)  
[MINX Function &#40;DAX&#41;](minx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
