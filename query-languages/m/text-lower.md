---
title: "Text.Lower | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Lower

## Syntax

<pre>
Text.Lower(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About  
Returns the result of converting all characters in `text` to lowercase. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get the lowercase version of "AbCd".

```powerquery-m
Text.Lower("AbCd")
```

`"abcd"`
