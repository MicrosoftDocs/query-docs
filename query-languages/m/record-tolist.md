---
description: "Learn more about: Record.ToList"
title: "Record.ToList"
ms.date: 3/9/2022
---
# Record.ToList

## Syntax

<pre>
Record.ToList(<b>record</b> as record) as list
</pre>

## About

Returns a list of values containing the field values from the input `record`.

## Example 1

Extract the field values from a record.

**Usage**

```powerquery-m
Record.ToList([A = 1, B = 2, C = 3])
```

**Output**

`{1, 2, 3}`
