---
title: "Text.Combine | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Combine

  
## About  
Returns a text value that is the result of joining all text values with each value separated by a separator.  
  
```  
Text.Combine(text as list,  separator as nullable text) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The list of text to combine.|  
|separator|The separator to use when combining.  This will only appear between the specified text values, not at the beginning or the end.|  
  
## Example  
  
```  
Text.Combine({"a", "b", "c"}, ",") equals "a,b,c"  
```  
