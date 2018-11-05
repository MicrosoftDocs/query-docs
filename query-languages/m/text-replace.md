---
title: "Text.Replace | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Replace

  
## About  
Replaces all occurrences of a substring with a new text value.  
  
## Syntax

<pre>
Text.Replace (text as nullable text, old as text, new as text) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|old|The text to replace.|  
|new|The replacement text.|  
  
## Example  
  
```powerquery-m
Text.Replace("Thisisanorange", "orange", "apple") equals "Thisisanapple"  
```  
