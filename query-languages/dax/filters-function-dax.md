---
title: "FILTERS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# FILTERS

Returns the values that are directly applied as filters to *columnName*.  
  
## Syntax
  
```dax
FILTERS(<columnName>)  
```
  
### Parameters

|Term  |Description|  
|---------|---------|
|columnName      | The name of an existing column, using standard DAX syntax. It cannot be an expression.  |

## Return value

The values that are directly applied as filters to *columnName*.  
  
## Remarks
  
## Example

The following example shows how to determine the number of direct filters a column has.  
  
```dax
= COUNTROWS(FILTERS(ResellerSales_USD[ProductKey]))  
```

This example lets you know how many direct filters on ResellerSales_USD[ProductKey] have been applied to the context where the expression is being evaluated.  
