---
title: "Text.Middle | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Middle

## Syntax

<pre>
Text.Middle(text as nullable text, start as number, optional count as nullable number) as nullable text  
</pre>
  
## About  
Returns count characters, or through the end of text; at the offset start.  
  
### Example 1  
Find the substring from the text "Hello World" starting at index 6 spanning 5 characters.  
  
```powerquery-m
Text.Middle("Hello World", 6, 5)  
```  
  
`
Equals: "World"  
`  
