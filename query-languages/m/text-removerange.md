---
title: "Text.RemoveRange | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.RemoveRange

## Syntax

<pre>
Text.RemoveRange(<b>text</b> as nullable text, <b>offset</b> as number, optional <b>count</b> as nullable number) as nullable text
</pre>
  
## About  
Returns a copy of the text value `text` with all the characters from position `offset` removed. An optional parameter, `count` can by used to specify the number of characters to remove. The default value of `count` is 1. Position values start at 0.

## Example 1
Remove 1 character from the text value "ABEFC" at position 2.

```powerquery-m
Text.RemoveRange("ABEFC", 2)
```

`"ABFC"`

## Example 2
Remove two characters from the text value "ABEFC" starting at position 2.

```powerquery-m
Text.RemoveRange("ABEFC", 2, 2)
```

`"ABC"`
