---
title: "LEN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# LEN
Returns the number of characters in a text string.  
  
## Syntax  
  
```dax
LEN(<text>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text|The text whose length you want to find, or a column that contains text. Spaces count as characters.|  
  
## Return value  
A whole number indicating the number of characters in the text string.  
  
  
  
## Remarks  
Whereas Microsoft Excel has different functions for working with single-byte and double-byte character languages, DAX uses Unicode and stores all characters with the same length.  
  
Therefore, LEN always counts each character as 1, no matter what the default language setting is.  
  
If you use LEN with a column that contains non-text values, such as dates or Booleans, the function implicitly casts the value to text, using the current column format.  
  
## Example  
The following formula sums the lengths of addresses in the columns, [AddressLine1] and [AddressLine2].  
  
```dax
=LEN([AddressLine1])+LEN([AddressLin2])  
  
