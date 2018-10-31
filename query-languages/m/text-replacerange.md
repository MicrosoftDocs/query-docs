---
title: "Text.ReplaceRange | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.ReplaceRange

  
## About  
Replaces length characters in a text value starting at a zero-based offset with the new text value.  
  
## Syntax

<pre>
Text.ReplaceRange(text as nullable text, offset as number, length as number, newText as text) as nullable text  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|offset|The beginning of the range.|  
|length|The length of the range.|  
|newText|The replacement text.|  
  
## Example  
  
```powerquery-m
Text.ReplaceRange("abcdef", 2, 3, "xyz") equals "abxyzf"  
```  
