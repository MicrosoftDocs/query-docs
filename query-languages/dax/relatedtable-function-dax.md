---
title: "RELATEDTABLE Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.RELATEDTABLE.f1"
helpviewer_keywords: 
  - "RELATEDTABLE function"
ms.assetid: 0f741322-e125-4d17-8444-7d1941a332f8
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# RELATEDTABLE Function (DAX)
Evaluates a table expression in a context modified by the given filters.  
  
## Syntax  
  
```  
RELATEDTABLE(<tableName>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**tableName**|The name of an existing table using standard DAX syntax. It cannot be an expression.|  
  
## Return Value  
A table of values.  
  
## Remarks  
The RELATEDTETABLE function changes the context in which the data is filtered, and evaluates the expression in the new context that you specify.  
  
This function is a shortcut for CALCULATETABLE function with no logical expression.  
  
## Example  
The following example uses the RELATEDTABLE function to create a calculated column with the Internet Sales in the Product Category table.  
  
The following table shows the results of using the code shown here.  
  
|||||  
|-|-|-|-|  
|Product Category Key|Product Category AlternateKey|Product Category Name|Internet Sales|  
|1|1|Bikes|$28,318,144.65|  
|2|2|Components||  
|3|3|Clothing|$339,772.61|  
|4|4|Accessories|$700,759.96|  
  
```  
= SUMX( RELATEDTABLE('InternetSales_USD')  
     , [SalesAmount_USD])  
```  
  
## See Also  
[CALCULATETABLE Function &#40;DAX&#41;](calculatetable-function-dax.md)  
[Filter Functions &#40;DAX&#41;](filter-functions-dax.md)  
  
