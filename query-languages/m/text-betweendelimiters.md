---
description: "Learn more about: Text.BetweenDelimiters"
title: "Text.BetweenDelimiters"
ms.subservice: m-source
---
# Text.BetweenDelimiters

## Syntax

<pre>
Text.BetweenDelimiters(<b>text</b> as nullable text, <b>startDelimiter</b> as text, <b>endDelimiter</b> as text, optional <b>startIndex</b> as any, optional <b>endIndex</b> as any) as any
</pre>

## About

Returns the portion of `text` between the specified `startDelimiter` and `endDelimiter`. An optional numeric `startIndex` indicates which occurrence of the `startDelimiter` should be considered. An optional list `startIndex` indicates which occurrence of the `startDelimiter` should be considered, as well as whether indexing should be done from the start or end of the input. The `endIndex` is similar, except that indexing is done relative to the `startIndex`.

## Example 1

Get the portion of "111 (222) 333 (444)" between the (first) open parenthesis and the (first) closed parenthesis that follows it.

**Usage**

```powerquery-m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")")
```

**Output**

`"222"`

## Example 2

Get the portion of "111 (222) 333 (444)" between the second open parenthesis and the first closed parenthesis that follows it.

**Usage**

```powerquery-m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")", 1, 0)
```

**Output**

`"444"`

## Example 3

Get the portion of "111 (222) 333 (444)" between the second open parenthesis from the end and the second closed parenthesis that follows it.

**Usage**

```powerquery-m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")", {1, RelativePosition.FromEnd}, {1, RelativePosition.FromStart})
```

**Output**

`"222) 333 (444"`
