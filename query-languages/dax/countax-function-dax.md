---
title: "COUNTAX function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# COUNTAX function (DAX)
The COUNTAX function counts nonblank results when evaluating the result of an expression over a table. That is, it works just like the COUNTA function, but is used to iterate through the rows in a table and count rows where the specified expressions results in a nonblank result.  
  
## Syntax  
  
```dax
COUNTAX(<table>,<expression>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return value  
A whole number.  
  
## Remarks  
Like the COUNTA function, the COUNTAX function counts cells containing any type of information, including other expressions.  
  
For example, if the column contains an expression that evaluates to an empty string, the COUNTAX function treats that result as nonblank. Usually the COUNTAX function does not count empty cells but in this case the cell contains a formula, so it is counted.  
  
If you do not need to count logical values or text, use the COUNTX function instead.  
  
Whenever the function finds no rows to aggregate, the function returns a blank. However, if there are rows, but none of them meet the specified criteria, the function returns 0. Microsoft Excel also returns 0 if no rows are found that meet the condition.  
  
## Example  
The following example counts the number of nonblank rows in the column, Phone, using the table that results from filtering the Reseller table on [Status] = **Active**.  
  
```dax
=COUNTAX(FILTER('Reseller',[Status]="Active"),[Phone])  
```
  
## See also  
[COUNT function &#40;DAX&#41;](count-function-dax.md)  
[COUNTA function &#40;DAX&#41;](counta-function-dax.md)  
[COUNTAX function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
