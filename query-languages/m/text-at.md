---
title: "Text.At | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Text.At

## Syntax

<pre>
Text.At(<b>text</b> as nullable text, <b>index</b> as number) as nullable text 
</pre>
  
## About  
Returns the character in the text value, `text` at position `index`. The first character in the text is at position 0.

## Example 1
Find the character at position 4 in string "Hello, World".

```powerquery-m
Text.At("Hello, World", 4)
```

`"o"`
