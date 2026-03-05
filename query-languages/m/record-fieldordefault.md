---
description: "Learn more about: Record.FieldOrDefault"
title: "Record.FieldOrDefault"
ms.subservice: m-source
ms.topic: reference
---
# Record.FieldOrDefault

## Syntax

<pre>
Record.FieldOrDefault(
    <b>record</b> as nullable record,
    <b>field</b> as text,
    optional <b>defaultValue</b> as any
) as any
</pre>

## About
Returns the value of the specified field `field` in the record `record`. If the field is not found, the optional `defaultValue` is returned.

## Example 1

Find the value of field "Phone" in the record, or return null if it doesn't exist.

**Usage**

```powerquery-m
Record.FieldOrDefault([CustomerID = 1, Name = "Bob"], "Phone")
```

**Output**

`null`

## Example 2

Find the value of field "Phone" in the record, or return the default if it doesn't exist.

**Usage**

```powerquery-m
Record.FieldOrDefault([CustomerID = 1, Name = "Bob"], "Phone", "123-4567")
```

**Output**

`"123-4567"`
