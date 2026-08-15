---
description: "Learn more about: Value.Metadata"
title: "Value.Metadata"
ms.subservice: m-source
ms.topic: reference
---

# Value.Metadata

## Syntax

<pre>
Value.Metadata(<b>value</b> as any) as any
</pre>

## About

Returns a record containing the input's metadata.

## Example

Return the number value's metadata record.

**Usage**

```powerquery-m
let
    valueWithMetadata = 1 meta [text = "one"]
in
    Value.Metadata(valueWithMetadata)
```

**Output**

`[text = "one"]`
