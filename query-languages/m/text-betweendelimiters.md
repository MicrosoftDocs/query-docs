---
title: "Text.BetweenDelimiters | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.BetweenDelimiters

## Syntax

<pre>
Text.BetweenDelimiters(**text** as nullable text, **startDelimiter** as text, **endDelimiter** as text, optional **startIndex** as any, optional **endIndex** as any) as any
</pre>

## About
Returns the portion of `text` between the specified `startDelimiter` and `endDelimiter`. An optional numeric `startIndex` indicates which occurrence of the `startDelimiter` should be considered. An optional list `startIndex` indicates which occurrence of the `startDelimiter` should be considered, as well as whether indexing should be done from the start or end of the input. The `endIndex` is similar, except that indexing is done relative to the `startIndex`.

## Example 1
Get the portion of "111 (222) 333 (444)" between the (first) open parenthesis and the (first) closed parenthesis that follows it.

```powerquery-m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")")
```

`"222"`

## Example 2
Get the portion of "111 (222) 333 (444)" between the second open parenthesis and the first closed parenthesis that follows it.

```powerquery-m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")", 1, 0)
```

`"444"`

## Example 3
Get the portion of "111 (222) 333 (444)" between the second open parenthesis from the end and the second closed parenthesis that follows it.

```powerquery-m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")", {1, RelativePosition.FromEnd}, {1, RelativePosition.FromStart})
```

`"222) 333 (444"`

  
