---
title: "Text.Middle | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Text.Middle

## Syntax

<pre>
Text.Middle(<b>text</b> as nullable text, <b>start</b> as number, optional <b>count</b> as nullable number) as nullable text
</pre>
  
## About  
Returns `count` characters, or through the end of `text`; at the offset `start`.

## Example 1
Find the substring from the text "Hello World" starting at index 6 spanning 5 characters.

```powerquery-m
Text.Middle("Hello World", 6, 5)
```

`"World"`

## Example 2
Find the substring from the text "Hello World" starting at index 6 through the end.

```powerquery-m
Text.Middle("Hello World", 6, 20)
```

`"World"`
