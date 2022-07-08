---
description: "Learn more about: FILTERS"
title: "FILTERS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

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

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example shows how to determine the number of direct filters a column has.  
  
```dax
= COUNTROWS(FILTERS(ResellerSales_USD[ProductKey]))  
```

This example lets you know how many direct filters on ResellerSales_USD[ProductKey] have been applied to the context where the expression is being evaluated.  
