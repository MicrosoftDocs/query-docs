---
title: "COUNTA function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# COUNTA

The COUNTA function counts the number of cells in a column that are not empty.  
  
## Syntax  
  
```dax
COUNTA(<column>)  
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the values to be counted|  
  
## Return value

A whole number.  
  
## Remarks  
  
When the function does not find any rows to count, the function returns a blank.
  
## Example

The following example returns all rows in the `Reseller` table that have any kind of value in the column that stores phone numbers. Because the table name does not contain any spaces, the quotation marks are optional.  
  
```dax
= COUNTA('Reseller'[Phone])  
```
  
## See also

[COUNT function &#40;DAX&#41;](count-function-dax.md)  
[COUNTAX function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
