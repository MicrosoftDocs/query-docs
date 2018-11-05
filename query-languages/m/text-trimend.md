---
title: "Text.TrimEnd | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.TrimEnd

  
## About  
Removes any occurrences of the characters specified in trimChars from the end of the original text value.  
  
## Syntax

<pre>
Text.TrimEnd(text as nullable text,  optional trimChars as nullable list) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to trim from.|  
|optional trimChars|A character value or a list of character values. If trimChars is not specified, then whitespace characters are trimmed.|  
  
