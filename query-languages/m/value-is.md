---
description: "Learn more about: Value.Is"
title: "Value.Is"
ms.date: 3/14/2022
---
# Value.Is

## Syntax

<pre>
Value.Is(<b>value</b> as any, <b>type</b> as type) as logical
</pre>
  
## About

Determines whether a value is compatible with the specified type. This is equivalent to the "is" operator in M, with the exception that it can accept identifier type references such as Number.Type.

## Example 1

Compare two ways of determining if a number is compatible with type number.

**Usage**

```powerquery-m
Value.Is(123, Number.Type) = (123 is number)
```

**Output**

`true`
