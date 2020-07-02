---
title: "COUNTBLANK function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# COUNTBLANK

Counts the number of blank cells in a column.  
  
## Syntax  
  
```dax
COUNTBLANK(<column>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the blank cells to be counted.|  
  
## Return value

A whole number. If no rows are found that meet the condition, blanks are returned.  
  
## Remarks

- The only argument allowed to this function is a column. You can use columns containing any type of data, but only blank cells are counted. Cells that have the value zero (0) are not counted, as zero is considered a numeric value and not a blank.  
  
- Whenever there are no rows to aggregate, the function returns a blank.  However, if there are rows, but none of them meet the specified criteria, the function returns 0. Microsoft Excel also returns a zero if no rows are found that meet the conditions.  
  
- In other words, if the COUNTBLANK function finds no blanks, the result will be zero, but if there are no rows to check, the result will be blank.  
  
- This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example

The following example shows how to count the number of rows in the table Reseller that have blank values for BankName.  
  
```dax
= COUNTBLANK(Reseller[BankName])  
```

To count logical values or text, use the COUNTA or COUNTAX functions.  
  
## See also

[COUNT function &#40;DAX&#41;](count-function-dax.md)  
[COUNTA function &#40;DAX&#41;](counta-function-dax.md)  
[COUNTAX function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
