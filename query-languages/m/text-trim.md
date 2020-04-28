---
title: "Text.Trim | Microsoft Docs"
ms.date: 4/22/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Text.Trim

## Syntax

<pre>
Text.Trim(<b>text</b> as nullable text, optional <b>trim</b> as any) as nullable text
</pre>
  
## About  
Returns the result of removing all leading and trailing whitespace from text value `text`.

## Example 1
Remove leading and trailing whitespace from " a b c d ".

```powerquery-m
Text.Trim("     a b c d    ")
```

`"a b c d"`
