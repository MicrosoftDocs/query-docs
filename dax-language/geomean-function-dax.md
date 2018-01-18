---
title: "GEOMEAN Function (DAX) | Microsoft Docs"
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
ms.assetid: 3cfcc687-b4b0-44a3-a9f0-28b7f0a84e05
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# GEOMEAN Function (DAX)
> [!NOTE]  
> This function is included in SQL Server 2016 Analysis Services (SSAS), Power Pivot in Excel 2016, and Power BI Desktop only. Information provided here is subject to change.  
  
Returns the geometric mean of the numbers in a column.  
  
To return the geometric mean of an expression evaluated for each row in a table, use [GEOMEANX Function &#40;DAX&#41;](../DAX/geomeanx-function-dax.md).  
  
## Syntax  
  
```  
GEOMEAN(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the numbers for which the geometric mean is to be computed.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
GEOMEAN( Table[Column] ) is equivalent to GEOMEANX( Table, Table[Column] )  
  
## Example  
The following computes the geometric mean of the Return column in the Investment table:  
  
```  
=GEOMEAN( Investment[Return] )  
```  
  
## See Also  
[GEOMEANX Function &#40;DAX&#41;](../DAX/geomeanx-function-dax.md)  
  
