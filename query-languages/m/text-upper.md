---
title: "Text.Upper | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Upper

## Syntax

<pre>
Text.Upper(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>  
  
## About  
Returns the result of converting all characters in `text` to uppercase.

## Example 1
Get the uppercase version of "aBcD".

```powerquery-m
Text.Upper("aBcD")
```

`"ABCD"`
