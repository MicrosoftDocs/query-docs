---
title: "Text.ToList | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.ToList

  
## About  
Returns a list of characters from a text value.  
  
## Syntax

<pre>
Text.ToList(text as text) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Text|The text to parse through.|  
  
## Example  
  
```powerquery-m
Text.ToList("abc") equals {"a","b","c"}  
```  
