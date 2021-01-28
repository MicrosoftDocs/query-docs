---
description: "Learn more about: Text.PositionOfAny"
title: "Text.PositionOfAny | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.PositionOfAny

## Syntax

<pre>
Text.PositionOfAny(<b>text</b> as text, <b>characters</b> as list, optional <b>occurrence</b> as nullable number) as any 
</pre>
  
## About  
Returns the position of the first occurrence of any of the characters in the character list `text` found in the text value `characters`. An optional parameter `occurrence` may be used to specify which occurrence position to return.

## Example 1
Find the position of "W" in text "Hello, World!".

```powerquery-m
Text.PositionOfAny("Hello, World!", {"W"})
```

`7`

## Example 2
Find the position of "W" or "H" in text "Hello, World!".

```powerquery-m
Text.PositionOfAny("Hello, World!", {"H", "W"})
```

`0`
