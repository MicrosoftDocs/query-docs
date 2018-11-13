---
title: "Text.Lower | Microsoft Docs"
ms.date: 11/13/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Lower

  
## About  
Returns the result of converting all characters in `text` to lowercase.
  
## Syntax

<pre> 
Text.Lower(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text 
</pre>
  
## Example  

Get the lowercase version of "AbCd".

```powerquery-m
Text.Lower("AbCd")
```

`"abcd"`
  
