---
description: "Learn more about: List.AnyTrue"
title: "List.AnyTrue"
ms.subservice: m-source
---
# List.AnyTrue

## Syntax

<pre>
List.AnyTrue(<b>list</b> as list) as logical
</pre>

## About

Returns true if any expression in the list `list` is true.

## Example 1

Determine if any of the expressions in the list {true, false, 2 > 0} are true.

**Usage**

```powerquery-m
List.AnyTrue({true, false, 2>0})
```

**Output**

`true`

## Example 2

Determine if any of the expressions in the list {2 = 0, false, 2 < 0} are true.

**Usage**

```powerquery-m
List.AnyTrue({2 = 0, false, 2 < 0})
```

**Output**

`false`
