---
title: "FILTERS Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.FILTERS.f1"
helpviewer_keywords: 
  - "FILTERS function"
ms.assetid: 7576afcc-4e39-41e3-98b8-6daabd44b1de
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
