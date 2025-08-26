---
description: "Learn more about: Text.AfterDelimiter"
title: "Text.AfterDelimiter"
ms.subservice: m-source
---
# Text.AfterDelimiter

## Syntax

<pre>
Text.AfterDelimiter(
    <b>text</b> as nullable text,
    <b>delimiter</b> as text,
    optional <b>index</b> as any
) as any
</pre>

## About

Returns the portion of `text` after the specified `delimiter`. An optional numeric `index` indicates which occurrence of the `delimiter` should be considered. An optional list `index` indicates which occurrence of the `delimiter` should be considered, as well as whether indexing should be done from the start or end of the input.

## Example 1

Get the portion of "111-222-333" after the (first) hyphen.

**Usage**

```powerquery-m
Text.AfterDelimiter("111-222-333", "-")
```

**Output**

`"222-333"`

## Example 2

Get the portion of "111-222-333" after the second hyphen.

**Usage**

```powerquery-m
Text.AfterDelimiter("111-222-333", "-", 1)
```

**Output**

`"333"`

## Example 3

Get the portion of "111-222-333" after the second hyphen from the end.

**Usage**

```powerquery-m
Text.AfterDelimiter("111-222-333", "-", {1, RelativePosition.FromEnd})
```

**Output**

`"222-333"`
