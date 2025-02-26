---
description: "Learn more about: Value.RemoveMetadata"
title: "Value.RemoveMetadata"
ms.subservice: m-source
---
# Value.RemoveMetadata

## Syntax

<pre>
Value.RemoveMetadata(<b>value</b> as any, optional <b>metaValue</b> as any) as any
</pre>

## About

Strips the input of metadata.

## Example 1

Remove all metadata from a text value.

**Usage**

```powerquery-m
Value.Metadata(
    Value.RemoveMetadata("abc" meta [a = 1, b = 2])
)
```

**Output**

`[]`

## Example 2

Remove only one field of metadata from a text value.

**Usage**

```powerquery-m
Value.Metadata(
    Value.RemoveMetadata("abc" meta [a = 1, b = 2], {"a"})
)
```

**Output**

`[b = 2]`
