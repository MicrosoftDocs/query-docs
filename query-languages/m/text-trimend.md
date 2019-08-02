---
title: "Text.TrimEnd | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.TrimEnd

## Syntax

<pre>
Text.TrimEnd(<b>text</b> as nullable text, optional <b>trim</b> as any) as nullable text
</pre>
  
## About  
Returns the result of removing all trailing whitespace from text value `text`.

## Example 1
Remove trailing whitespace from " a b c d ".

```powerquery-m
Text.TrimEnd(" a b c d ")
```

`" a b c d"`
