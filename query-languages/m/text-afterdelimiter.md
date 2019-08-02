---
title: "Text.AfterDelimiter | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.AfterDelimiter

## Syntax

<pre>
Text.AfterDelimiter(<b>text</b> as nullable text, <b>delimiter</b> as text, optional <b>index</b> as any) as any
</pre>

## About
Returns the portion of `text` after the specified `delimiter`. An optional numeric `index` indicates which occurrence of the `delimiter` should be considered. An optional list `index` indicates which occurrence of the `delimiter` should be considered, as well as whether indexing should be done from the start or end of the input.

## Example 1
Get the portion of "111-222-333" after the (first) hyphen.

```powerquery-m
Text.AfterDelimiter("111-222-333", "-")
```

`"222-333"`

## Example 2
Get the portion of "111-222-333" after the second hyphen.

```powerquery-m
Text.AfterDelimiter("111-222-333", "-", 1)
```

`"333"`

## Example 3
Get the portion of "111-222-333" after the second hyphen from the end.

```powerquery-m
Text.AfterDelimiter("111-222-333", "-", {1, RelativePosition.FromEnd})
```

`"222-333"`
