---
description: "Learn more about: List.AllTrue"
title: "List.AllTrue"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.AllTrue

## Syntax

<pre>
List.AllTrue(<b>list</b> as list) as logical
</pre>
  
## About

Returns true if all expressions in the list `list` are true.

## Example 1

Determine if all the expressions in the list {true, true, 2 > 0} are true.

**Usage**

```powerquery-m
List.AllTrue({true, true, 2 > 0})
```

**Output**

`true`

## Example 2

Determine if all the expressions in the list {true, true, 2 < 0} are true.

**Usage**

```powerquery-m
List.AllTrue({true, false, 2 < 0})
```

**Output**

`false`
