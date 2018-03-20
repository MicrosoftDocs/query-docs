---
title: "MEDIAN Function (DAX) | Microsoft Docs"
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
ms.assetid: eb6949a0-9bd4-4de7-b77d-2863512314d7
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# MEDIAN Function (DAX)
  
Returns the median of numbers in a column.  
  
To return the median of an expresssion evaluated for each row in a table, use [MEDIANX Function &#40;DAX&#41;](medianx-function-dax.md).  
  
## Syntax  
  
```  
MEDIAN(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the numbers for which the median is to be computed.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
MEDIAN( Table[Column] ) is equivalent to MEDIANX( Table, Table[Column] ).  
  
## Example  
The following computes the median of a column named Age in a table named Customers:  
  
```  
=MEDIAN( Customers[Age] )  
```  
  
## See Also  
[MEDIANX Function &#40;DAX&#41;](medianx-function-dax.md)  
  
