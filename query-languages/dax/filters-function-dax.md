---
title: "FILTERS Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# FILTERS Function (DAX)
Returns the values that are directly applied as filters to *columnName*.  
  
## Syntax  
  
```  
FILTERS(<columnName>)  
```  
  
#### Parameters  
columnName  
The name of an existing column, using standard DAX syntax. It cannot be an expression.  
  
## Return Value  
The values that are directly applied as filters to *columnName*.  
  
## Remarks  
  
## Example  
The following example shows how to determine the number of direct filters a column has.  
  
```  
=COUNTROWS(FILTERS(ResellerSales_USD[ProductKey]))  
```  
The example above lets you know how many direct filters on ResellerSales_USD[ProductKey] have been applied to the context where the expression is being evaluated.  
  
