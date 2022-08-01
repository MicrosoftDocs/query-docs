---
description: "Learn more about: Type.IsNullable"
title: "Type.IsNullable"
ms.date: 3/14/2022
---
# Type.IsNullable

## Syntax

<pre>  
Type.IsNullable(<b>type</b> as type) as logical
</pre>
  
## About

Returns `true` if a type is a `nullable` type; otherwise, `false`.

## Example 1

Determine if `number` is nullable.

**Usage**

```powerquery-m
Type.IsNullable(type number)
```

**Output**

`false`

## Example 2

Determine if `type nullable number` is nullable.

**Usage**

```powerquery-m
Type.IsNullable(type nullable number)
```

**Output**

`true`
