---
description: "Learn more about: Type.ClosedRecord"
title: "Type.ClosedRecord"
ms.subservice: m-source
---
# Type.ClosedRecord

## Syntax

<pre>
Type.ClosedRecord(<b>type</b> as type) as type
</pre>
  
## About

Returns a closed version of the given `record` `type` (or the same type, if it is already closed).

## Example 1

Create a closed version of `type [ A = number,…]`.

**Usage**

```powerquery-m
Type.ClosedRecord(type [A = number, ...])
```

**Output**

`type [A = number]`
