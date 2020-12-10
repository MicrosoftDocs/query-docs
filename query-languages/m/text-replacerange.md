---
title: "Text.ReplaceRange | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.ReplaceRange

## Syntax

<pre>
Text.ReplaceRange(<b>text</b> as nullable text, <b>offset</b> as number, <b>count</b> as number, <b>newText</b> as text) as nullable text
</pre> 
  
## About  
Returns the result of removing a number of characters, `count`, from text value `text` beginning at position `offset` and then inserting the text value `newText` at the same position in `text`.

## Example 1
Replace a single character at position 2 in text value "ABGF" with new text value "CDE".

```powerquery-m
Text.ReplaceRange("ABGF", 2, 1, "CDE")
```

`"ABCDEF"`
