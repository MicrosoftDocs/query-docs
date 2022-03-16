---
description: "Learn more about: Value.As"
title: "Value.As | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Value.As

## Syntax

<pre>
Value.As(<b>value</b> as any, <b>type</b> as type) as any
</pre>
  
## About

Returns the value if it's compatible with the specified type. This is equivalent to the "as" operator in M, with the exception that it can accept identifier type references such as Number.Type.

## Example 1

Cast a number to a number.

**Usage**

```powerquery-m
Value.As(123, Number.Type)
```

**Output**

`123`

## Example 2

Attempt to cast a text value to a number.

**Usage**

```powerquery-m
Value.As("abc", type number)
```

**Output**

`[Expression.Error] We cannot convert the value "abc" to type Number.`  
