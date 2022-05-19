---
description: "Learn more about: Text.TrimStart"
title: "Text.TrimStart | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Text.TrimStart

## Syntax

<pre>
Text.TrimStart(<b>text</b> as nullable text, optional <b>trim</b> as any) as nullable text
</pre>
  
## About

Returns the result of removing all leading whitespace from text value `text`.

## Example 1

Remove leading whitespace from " a b c d ".

Usage**

```powerquery-m
Text.TrimStart("   a b c d    ")
```

**Output**

<pre>
"a b c d    "
</pre>
