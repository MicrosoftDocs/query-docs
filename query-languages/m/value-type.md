---
description: "Learn more about: Value.Type"
title: "Value.Type"
ms.subservice: m-source
---
# Value.Type

## Syntax

<pre>
Value.Type(<b>value</b> as any) as type
</pre>

## About

Returns the type of the given value.

* `value`: The value whose type is returned.

## Example 1

Return the type of the specified number.

**Usage**

```powerquery-m
Value.Type(243.448)
```

**Output**

`type number`

## Example 2

Return the type of the specified date.

**Usage**

```powerquery-m
Value.Type(#datetime(2010, 12, 31))
```

**Output**

`type date`

## Example 3

Return the type of the specified record.

**Usage**

```powerquery-m
Value.Type([a = 1, b = 2])
```

**Output**

`type record`

## Related content

* [Types and type conversion](type-conversion.md)
