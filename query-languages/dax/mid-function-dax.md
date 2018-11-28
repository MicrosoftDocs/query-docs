---
title: "MID function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MID function (DAX)
Returns a string of characters from the middle of a text string, given a starting position and length.  
  
## Syntax  
  
```dax
MID(<text>, <start_num>, <num_chars>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text|The text string from which you want to extract the characters, or a column that contains text.|  
|start_num|The position of the first character you want to extract. Positions start at 1.|  
|num_chars|The number of characters to return.|  
  
## Property Value/Return value  
A string of text of the specified length.  
  
## Remarks  
Whereas Microsoft Excel has different functions for working with single-byte and double-byte characters languages, DAX uses Unicode and stores all characters with the same length.  
  
## Example  
The following examples return the same results, the first 5 letters of the column, [ResellerName]. The first example uses the fully qualified name of the column and specifies the starting point; the second example omits the table name and the parameter, **num_chars**.  
  
```dax
=MID('Reseller'[ResellerName],5,1))  
=MID([ResellerName,5])  
```

The results are the same if you use the following formula:  
  
`=LEFT([ResellerName],5)`  
  
## See also  
[Text functions &#40;DAX&#41;](text-functions-dax.md)  
  
