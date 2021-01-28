---
description: "Learn more about: Text.Range"
title: "Text.Range | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Range

## Syntax

<pre>
Text.Range(<b>text</b> as nullable text, <b>offset</b> as number, optional <b>count</b> as nullable number) as nullable text 
</pre>
  
## About  
Returns the substring from the text `text` found at the offset `offset`. An optional parameter, `count`, can be included to specify how many characters to return. Throws an error if there aren't enough characters.

## Example 1
Find the substring from the text "Hello World" starting at index 6.

```powerquery-m
Text.Range("Hello World", 6)
```

`"World"`

## Example 2
Find the substring from the text "Hello World Hello" starting at index 6 spanning 5 characters.

```powerquery-m
Text.Range("Hello World Hello", 6, 5)
```

`"World"`
