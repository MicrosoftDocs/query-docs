---
description: "Learn more about: COUNTA"
title: "COUNTA function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

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
  
- When the function does not find any rows to count, the function returns a blank.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example returns all rows in the `Reseller` table that have any kind of value in the column that stores phone numbers. Because the table name does not contain any spaces, the quotation marks are optional.  
  
```dax
= COUNTA('Reseller'[Phone])  
```
  
## See also

[COUNT function](count-function-dax.md)  
[COUNTAX function](countax-function-dax.md)  
[COUNTX function](countx-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
