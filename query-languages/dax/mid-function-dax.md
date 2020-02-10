---
title: "MID function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 02/11/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# MID
Returns a string of characters from the middle of a text string, given a starting position and length.  
  
## Syntax  
  
```dax
MID(<text>, <start_num>, <num_chars>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text|The text string from which you want to extract the characters, or a column that contains text.|  
|start_num|The position of the first character you want to extract. Positions start at 1.|  
|num_chars|The number of characters to return.|  
  
## Property Value/Return value  
A string of text of the specified length.  
  
## Remarks  
Whereas Microsoft Excel has different functions for working with single-byte and double-byte characters languages, DAX uses Unicode and stores all characters with the same length.  
  
## Examples  

The following expression,

```dax
MID("abcde",2,3))
```

Returns **"bcd"**.

The following expression,

```dax
MID('Reseller'[ResellerName],1,5))
```

Returns the same result as `LEFT([ResellerName],5)`. Both expressions return the first 5 letters of column, `[ResellerName]`.
  
## See also  
[Text functions &#40;DAX&#41;](text-functions-dax.md)  
  
