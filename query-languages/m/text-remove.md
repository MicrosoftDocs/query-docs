---
title: "Text.Remove | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Remove

  
## About  
Removes all occurrences of a character or list of characters from a text value. The **removeChars** parameter can be a character value or a list of character values.  
  
```  
Text.Remove(text as nullable text, removeChars as any) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|removeChars|A character value or a list of character values to be removed.|  
  
## Examples  
  
```  
Text.Remove("a,b,;c",",")equals "ab;c"  
```  
  
```  
Text.Remove("a,b,;c",{",",";"}) equals "abc"  
```  
