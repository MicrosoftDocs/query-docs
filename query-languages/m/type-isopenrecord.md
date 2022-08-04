---
description: "Learn more about: Type.IsOpenRecord"
title: "Type.IsOpenRecord"
ms.date: 3/14/2022
---
# Type.IsOpenRecord

## Syntax

<pre>
Type.IsOpenRecord(<b>type</b> as type) as logical
</pre>
  
## About

Returns a `logical` indicating whether a record `type` is open.

## Example 1

Determine if the record `type [ A = number, ...]` is open.

**Usage**

```powerquery-m
Type.IsOpenRecord(type [A = number, ...])
```

**Output**

`true`
