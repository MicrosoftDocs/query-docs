---
title: "Text.Insert | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Insert

## Syntax

<pre>
Text.Insert(<b>text</b> as nullable text, <b>offset</b> as number, <b>newText</b> as text) as nullable text
</pre>
  
## About  
Returns the result of inserting text value `newText` into the text value `text` at position `offset`. Positions start at number 0.

## Example 1
Insert "C" between "B" and "D" in "ABD".

```powerquery-m
Text.Insert("ABD", 2, "C")
```

`"ABCD"`
