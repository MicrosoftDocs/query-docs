---
description: "Learn more about: Text.BeforeDelimiter"
title: "Text.BeforeDelimiter"
ms.date: 3/14/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Text.BeforeDelimiter("111-222-333", "-")
```

**Output**

`"111"`

## Example 2

Get the portion of "111-222-333" before the second hyphen.

**Usage**

```powerquery-m
Text.BeforeDelimiter("111-222-333", "-", 1)
```

**Output**

`"111-222"`

## Example 3

Get the portion of "111-222-333" before the second hyphen from the end.

**Usage**

```powerquery-m
Text.BeforeDelimiter("111-222-333", "-", {1, RelativePosition.FromEnd})
```

**Output**

`"111"`
