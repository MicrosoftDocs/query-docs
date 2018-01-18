---
title: "LEN Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.LEN.f1"
helpviewer_keywords: 
  - "LEN function"
ms.assetid: dfea34d7-1360-4b13-9cd5-3041e30ccfcc
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# LEN Function (DAX)
Returns the number of characters in a text string.  
  
## Syntax  
  
```  
LEN(<text>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text whose length you want to find, or a column that contains text. Spaces count as characters.|  
  
## Return Value  
A whole number indicating the number of characters in the text string.  
  
  
  
## Remarks  
Whereas Microsoft Excel has different functions for working with single-byte and double-byte character languages, DAX uses Unicode and stores all characters with the same length.  
  
Therefore, LEN always counts each character as 1, no matter what the default language setting is.  
  
If you use LEN with a column that contains non-text values, such as dates or Booleans, the function implicitly casts the value to text, using the current column format.  
  
## Example  
The following formula sums the lengths of addresses in the columns, [AddressLine1] and [AddressLine2].  
  
```  
=LEN([AddressLine1])+LEN([AddressLin2])  
  
