---
description: "Learn more about: COUNTAX"
title: "COUNTAX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# COUNTAX

The COUNTAX function counts non-blank results when evaluating the result of an expression over a table. That is, it works just like the COUNTA function, but is used to iterate through the rows in a table and count rows where the specified expressions results in a non-blank result.  
  
## Syntax  
  
```dax
COUNTAX(<table>,<expression>)  
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return value

A whole number.  
  
## Remarks

- Like the COUNTA function, the COUNTAX function counts cells containing any type of information, including other expressions. For example, if the column contains an expression that evaluates to an empty string, the COUNTAX function treats that result as non-blank. Usually the COUNTAX function does not count empty cells but in this case the cell contains a formula, so it is counted.  
  
- Whenever the function finds no rows to aggregate, the function returns a blank.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example counts the number of nonblank rows in the column, Phone, using the table that results from filtering the Reseller table on [Status] = **Active**.  
  
```dax
= COUNTAX(FILTER('Reseller',[Status]="Active"),[Phone])  
```
  
## See also

[COUNT function](count-function-dax.md)  
[COUNTA function](counta-function-dax.md)  
[COUNTX function](countx-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
