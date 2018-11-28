---
title: "AVERAGEA function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# AVERAGEA function (DAX)
Returns the average (arithmetic mean) of the values in a column. Handles text and non-numeric values.  
  
## Syntax  
  
```dax
AVERAGEA(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|A column that contains the values for which you want the average.|  
  
## Return value  
A decimal number.  
  
## Remarks  
The AVERAGEA function takes a column and averages the numbers in it, but also handles non-numeric data types according to the following rules:  
  
-   Values that evaluates to TRUE count as 1.  
  
-   Values that evaluate to FALSE count as 0 (zero).  
  
-   Values that contain non-numeric text count as 0 (zero).  
  
-   Empty text ("") counts as 0 (zero).  
  
If you do not want to include logical values and text representations of numbers in a reference as part of the calculation, use the AVERAGE function.  
  
Whenever there are no rows to aggregate, the function returns a blank.  However, if there are rows, but none of them meet the specified criteria, the function returns 0. Microsoft Excel also returns a zero if no rows are found that meet the conditions.  
  
## Example  
The following example returns the average of non-blank cells in the referenced column, given the following table. If you used the AVERAGE function, the mean would be 21/2; with the AVERAGEA function, the result is 22/5.  
  
|Transaction ID|Amount|Result|  
|------------------|----------|----------|  
|0000123|1|Counts as 1|  
|0000124|20|Counts as 20|  
|0000125|n/a|Counts as 0|  
|0000126||Counts as 0|  
|0000126|TRUE|Counts as 1|  
  
```dax
=AVERAGEA([Amount])  
```
  
## See also  
[AVERAGE function &#40;DAX&#41;](average-function-dax.md)  
[AVERAGEX function &#40;DAX&#41;](averagex-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
