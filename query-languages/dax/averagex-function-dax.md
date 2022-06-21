---
description: "Learn more about: AVERAGEX"
title: "AVERAGEX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# AVERAGEX

Calculates the average (arithmetic mean) of a set of expressions evaluated over a table.  
  
## Syntax  
  
```dax
AVERAGEX(<table>,<expression>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|Name of a table, or an expression that specifies the table over which the aggregation can be performed.|  
|expression|An expression with a scalar result, which will be evaluated for each row of the table in the first argument.|  
  
## Return value

A decimal number.  
  
## Remarks

- The AVERAGEX function enables you to evaluate expressions for each row of a table, and then take the resulting set of values and calculate its arithmetic mean. Therefore, the function takes a table as its first argument, and an expression as the second argument.  
  
- In all other respects, AVERAGEX follows the same rules as AVERAGE. You cannot include non-numeric or null cells. Both the table and expression arguments are required.  
  
- When there are no rows to aggregate, the function returns a blank.  When there are rows, but none of them meet the specified criteria, then the function returns 0.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example calculates the average freight and tax on each order in the InternetSales table, by first summing Freight plus TaxAmt in each row, and then averaging those sums.  
  
```dax
= AVERAGEX(InternetSales, InternetSales[Freight]+ InternetSales[TaxAmt])  
```

If you use multiple operations in the expression used as the second argument, you must use parentheses to control the order of calculations. For more information, see [DAX Syntax Reference](dax-syntax-reference.md).  
  
## See also

[AVERAGE function](average-function-dax.md)  
[AVERAGEA function](averagea-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
