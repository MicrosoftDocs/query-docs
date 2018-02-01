---
title: "COUNTAX Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.COUNTAX.f1"
helpviewer_keywords: 
  - "COUNTAX function"
ms.assetid: 0a329709-4a7d-4edf-a0b3-0254a4c52a88
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# COUNTAX Function (DAX)
The COUNTAX function counts nonblank results when evaluating the result of an expression over a table. That is, it works just like the COUNTA function, but is used to iterate through the rows in a table and count rows where the specified expressions results in a nonblank result.  
  
## Syntax  
  
```  
COUNTAX(<table>,<expression>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**table**|The table containing the rows for which the expression will be evaluated.|  
|**expression**|The expression to be evaluated for each row of the table.|  
  
## Return Value  
A whole number.  
  
## Remarks  
Like the COUNTA function, the COUNTAX function counts cells containing any type of information, including other expressions.  
  
For example, if the column contains an expression that evaluates to an empty string, the COUNTAX function treats that result as nonblank. Usually the COUNTAX function does not count empty cells but in this case the cell contains a formula, so it is counted.  
  
If you do not need to count logical values or text, use the COUNTX function instead.  
  
Whenever the function finds no rows to aggregate, the function returns a blank. However, if there are rows, but none of them meet the specified criteria, the function returns 0. Microsoft Excel also returns 0 if no rows are found that meet the condition.  
  
## Example  
The following example counts the number of nonblank rows in the column, Phone, using the table that results from filtering the Reseller table on [Status] = **Active**.  
  
```  
=COUNTAX(FILTER('Reseller',[Status]="Active"),[Phone])  
```  
  
## See Also  
[COUNT Function &#40;DAX&#41;](count-function-dax.md)  
[COUNTA Function &#40;DAX&#41;](counta-function-dax.md)  
[COUNTAX Function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX Function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
