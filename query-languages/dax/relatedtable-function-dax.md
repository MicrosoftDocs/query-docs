---
title: "RELATEDTABLE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# RELATEDTABLE

Evaluates a table expression in a context modified by the given filters.  
  
## Syntax  
  
```dax
RELATEDTABLE(<tableName>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|tableName|The name of an existing table using standard DAX syntax. It cannot be an expression.|  
  
## Return value

A table of values.  
  
## Remarks

- The RELATEDTETABLE function changes the context in which the data is filtered, and evaluates the expression in the new context that you specify.  
  
- This function is a shortcut for CALCULATETABLE function with no logical expression.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example uses the RELATEDTABLE function to create a calculated column with the Internet Sales in the Product Category table.  
  
The following table shows the results:  

|Product Category Key|Product Category AlternateKey|Product Category Name|Internet Sales|  
|-----|------|------|------|  
|1|1|Bikes|$28,318,144.65|  
|2|2|Components||  
|3|3|Clothing|$339,772.61|  
|4|4|Accessories|$700,759.96|  
  
```dax
= SUMX( RELATEDTABLE('InternetSales_USD')  
     , [SalesAmount_USD])  
```
  
## See also

[CALCULATETABLE](calculatetable-function-dax.md)  
[Filter functions](filter-functions-dax.md)
