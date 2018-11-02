---
title: "Text.PadStart | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.PadStart

  
## About  
Returns a text value padded at the beginning with pad to make it at least length characters.  If pad is not specified, whitespace is used as pad.  
  
## Syntax

<pre>
Text.PadStart(text as nullable text, length as number, optional pad as nullable text) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|length|The length to pad to.|  
|optional pad|The text to pad with.  If pad is not specified, whitespace is used as pad.|  
  
## Examples  
  
```powerquery-m 
Text.PadStart("xyz", 5, "a") equals "aaxyz"  
```  
  
```powerquery-m 
Text.PadStart("xyz", 9, "pad") equals error  
```  
