---
title: "Text.Upper | Microsoft Docs"
ms.date: 11/13/2018
ms.service: powerquery
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Upper

  
## About  
Returns the result of converting all characters in `text` to uppercase.

  
## Syntax

<pre> 
Text.Upper(**text** as nullable text, optional **culture** as nullable text) as nullable text
</pre>  
  
## Example

Get the uppercase version of "aBcD".

```powerquery-m
Text.Upper("aBcD")
```

`"ABCD"`
  
