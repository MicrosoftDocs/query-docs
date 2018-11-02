---
title: "Text.TrimStart | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.TrimStart

  
## About  
Removes any occurrences of the characters in trimChars from the start of the original text value.  
  
## Syntax

<pre>
Text.TrimStart(text as nullable text, optional trimChars as nullable list) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to trim from.|  
|optional trimChars|A character value or a list of character values.|  
  
## <a name="__toc360788916"></a>Remarks  
  
-   If trimChars is not specified, then whitespace characters are trimmed.  
  
