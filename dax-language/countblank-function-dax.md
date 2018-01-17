---
title: "COUNTBLANK Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.COUNTBLANK.f1"
helpviewer_keywords: 
  - "Blanks"
  - "COUNTBLANK function"
ms.assetid: 10b27d94-a89e-4bb3-8069-f939d8ba19e9
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# COUNTBLANK Function (DAX)
Counts the number of blank cells in a column.  
  
## Syntax  
  
```  
COUNTBLANK(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column that contains the blank cells to be counted.|  
  
## Return Value  
A whole number. If no rows are found that meet the condition, blanks are returned.  
  
## Remarks  
The only argument allowed to this function is a column. You can use columns containing any type of data, but only blank cells are counted. Cells that have the value zero (0) are not counted, as zero is considered a numeric value and not a blank.  
  
Whenever there are no rows to aggregate, the function returns a blank.  However, if there are rows, but none of them meet the specified criteria, the function returns 0. Microsoft Excel also returns a zero if no rows are found that meet the conditions.  
  
In other words, if the COUNTBLANK function finds no blanks, the result will be zero, but if there are no rows to check, the result will be blank.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following example shows how to count the number of rows in the table Reseller that have blank values for BankName.  
  
```  
=COUNTBLANK(Reseller[BankName])  
```  
To count logical values or text, use the COUNTA or COUNTAX functions.  
  
## See Also  
[COUNT Function &#40;DAX&#41;](../DAX/count-function-dax.md)  
[COUNTA Function &#40;DAX&#41;](../DAX/counta-function-dax.md)  
[COUNTAX Function &#40;DAX&#41;](../DAX/countax-function-dax.md)  
[COUNTX Function &#40;DAX&#41;](../DAX/countx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](../DAX/statistical-functions-dax.md)  
  
