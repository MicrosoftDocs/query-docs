---
title: "Text.BeforeDelimiter | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.BeforeDelimiter

## Syntax

<pre>
Text.BeforeDelimiter(**text** as nullable text, **delimiter** as text, optional **index** as any) as any
</pre>

## About
Returns the portion of `text` before the specified `delimiter`. An optional numeric `index` indicates which occurrence of the `delimiter` should be considered. An optional list `index` indicates which occurrence of the `delimiter` should be considered, as well as whether indexing should be done from the start or end of the input.

## Example 1
Get the portion of "111-222-333" before the (first) hyphen.

```powerquery-m
Text.BeforeDelimiter("111-222-333", "-")
```

`"111"`

## Example 2
Get the portion of "111-222-333" before the second hyphen.

```powerquery-m
Text.BeforeDelimiter("111-222-333", "-", 1)
```

`"111-222"`

## Example 3
Get the portion of "111-222-333" before the second hyphen from the end.

```powerquery-m
Text.BeforeDelimiter("111-222-333", "-", {1, RelativePosition.FromEnd})
```

`"111"`


  
