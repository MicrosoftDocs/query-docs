---
title: "GEOMEANX Function (DAX) | Microsoft Docs"
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
ms.assetid: f0699a1c-5a43-4c4f-adc1-551390bbd64e
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# GEOMEANX Function (DAX)
  
Returns the geometric mean of an expression evaluated for each row in a table.  
  
To return the geometric mean of the numbers in a column, use [GEOMEAN Function &#40;DAX&#41;](geomean-function-dax.md).  
  
## Syntax  
  
```  
GEOMEANX(<table>, <expression>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The GEOMEANX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the geometric mean, or an expression that evaluates to a column.  
  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
## Example  
The following computes the geometric mean of the ReturnPct column in the Investments table:  
  
```  
=GEOMEANX( Investments, Investments[ReturnPct] + 1 )  
```  
  
## See Also  
[GEOMEAN Function &#40;DAX&#41;](geomean-function-dax.md)  
  
