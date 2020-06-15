---
title: "CONCATENATEX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/15/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# CONCATENATEX
  
Concatenates the result of an expression evaluated for each row in a table.  
  
## Syntax  
  
```dax
CONCATENATEX(<table>, <expression>, [delimiter])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
|delimiter|(optional) A separator to use during concatenation.|  
  
## Return value

A text string.  
  
## Remarks

This function takes as its first argument a table or an expression that returns a table. The second argument is a column that contains the values you want to concatenate, or an expression that returns a value.  
  
## Example

Employees table  
  
|FirstName|LastName|  
|-------------|------------|  
|Alan|Brewer|  
|Michael|Blythe|  

The following formula:  

```dax
CONCATENATEX(Employees, [FirstName] &amp; " " &amp; [LastName], ",")  
```
  
Returns:  
"Alan Brewer, Michael Blythe"  
  
