---
title: "Text.Lower | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Text.Lower

## Syntax

<pre>
Text.Lower(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About  
Returns the result of converting all characters in `text` to lowercase.

## Example 1
Get the lowercase version of "AbCd".

```powerquery-m
Text.Lower("AbCd")
```

`"abcd"`
