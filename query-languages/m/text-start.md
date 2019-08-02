---
title: "Text.Start | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Start

## Syntax

<pre>
Text.Start(<b>text</b> as nullable text, <b>count</b> as number) as nullable text
</pre>
  
## About  
Returns the first `count` characters of `text` as a text value.

## Example 1
Get the first 5 characters of "Hello, World".

```powerquery-m
Text.Start("Hello, World", 5)
```

`"Hello"`
