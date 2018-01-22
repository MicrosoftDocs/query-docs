---
title: "VAR.P Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.VAR.P.f1"
helpviewer_keywords: 
  - "VAR.P Function (DAX)"
ms.assetid: 378d1486-2ea8-4978-8186-aa266a8bf5a7
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# VAR.P Function (DAX)
Returns the variance of the entire population.  
  
## Syntax  
  
```  
VAR.P(<columnName>)  
```  
  
#### Parameters  
columnName  
The name of an existing column using standard DAX syntax, usually fully qualified. It cannot be an expression.  
  
## Return Value  
A number with the variance of the entire population.  
  
## Remarks  
  
1.  VAR.P assumes that the column refers the entire population. If your data represents a sample of the population, then compute the variance by using VAR.S.  
  
2.  VAR.P uses the following formula:  
  
    ∑(x - x̃)²/n  
  
    where x̃ is the average value of x for the entire population  
  
    and n is the population size  
  
3.  Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
4.  An error is returned if *columnName* contains less than 2 non-blank rows  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example shows the formula for a measure that estimates the variance of the SalesAmount_USD column from the InternetSales_USD table, for the entire population.  
  
```  
=VAR.P(InternetSales_USD[SalesAmount_USD])  
```  
