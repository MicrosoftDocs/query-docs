---
title: "Text.BeforeDelimiter | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.BeforeDelimiter

## Syntax

<pre>
Text.BeforeDelimiter(<b>text</b> as nullable text, <b>delimiter</b> as text, optional <b>index</b> as any) as any
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
