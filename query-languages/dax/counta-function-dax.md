---
title: "COUNTA Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# COUNTA Function (DAX)
The COUNTA function counts the number of cells in a column that are not empty. It counts not just rows that contain numeric values, but also rows that contain nonblank values, including text, dates, and logical values.  
  
## Syntax  
  
```dax
COUNTA(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column that contains the values to be counted|  
  
## Return Value  
A whole number.  
  
## Remarks  
If you do not need to count cells that contain logical values or text (in other words, if you want to count only cells that contain numbers), use the COUNT or COUNTX functions.  
  
When the function does not find any rows to count, the function returns a blank.  When there are rows, but none of them meet the specified criteria, then the function returns 0.  
  
## Example  
The following example returns all rows in the `Reseller` table that have any kind of value in the column that stores phone numbers. Because the table name does not contain any spaces, the quotation marks are optional.  
  
```dax
=COUNTA('Reseller'[Phone])  
```
  
## See Also  
[COUNT Function &#40;DAX&#41;](count-function-dax.md)  
[COUNTA Function &#40;DAX&#41;](counta-function-dax.md)  
[COUNTAX Function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX Function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
