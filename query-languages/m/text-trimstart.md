---
title: "Text.TrimStart | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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

```powerquery-m
Text.TrimStart(" a b c d ")
```

`"a b c d "`
