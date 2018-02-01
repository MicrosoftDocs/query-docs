---
title: "SUM Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.SUM.f1"
helpviewer_keywords: 
  - "aggregates"
  - "SUM function"
ms.assetid: 4710ea3c-024f-4b3e-9d9d-3ca19db1edd1
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# SUM Function (DAX)
Adds all the numbers in a column.  
  
## Syntax  
  
```  
SUM(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column that contains the numbers to sum.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
If any rows contain non-numeric values, blanks are returned.  
  
If you want to filter the values that you are summing, you can use the SUMX function and specify an expression to sum over.  
  
## Example  
The following example adds all the numbers that are contained in the column, Amt, from the table, Sales.  
  
```  
=SUM(Sales[Amt])  
```  
  
## See Also  
[SUMX Function &#40;DAX&#41;](sumx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
