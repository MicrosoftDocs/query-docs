---
description: "Learn more about: COUNTBLANK"
title: "COUNTBLANK function (DAX) | Microsoft Docs"
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
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example shows how to count the number of rows in the table Reseller that have blank values for BankName.  
  
```dax
= COUNTBLANK(Reseller[BankName])  
```

To count logical values or text, use the COUNTA or COUNTAX functions.  
  
## See also

[COUNT function](count-function-dax.md)  
[COUNTA function](counta-function-dax.md)  
[COUNTAX function](countax-function-dax.md)  
[COUNTX function](countx-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
