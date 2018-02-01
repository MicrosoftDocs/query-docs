---
title: "UPPER Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.UPPER.f1"
helpviewer_keywords: 
  - "UPPER function"
ms.assetid: 35a9badc-153e-4e05-93a5-254b1400126a
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# UPPER Function (DAX)
Converts a text string to all uppercase letters  
  
## Syntax  
  
```  
UPPER (<text>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text you want converted to uppercase, or a reference to a column that contains text.|  
  
## Property Value/Return Value  
Same text, in uppercase.  
  
## Example  
The following formula converts the string in the column, [ProductCode], to all uppercase. Non-alphabetic characters are not affected.  
  
```  
=UPPER(['New Products'[Product Code])  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
[LOWER Function &#40;DAX&#41;](lower-function-dax.md)  
  
