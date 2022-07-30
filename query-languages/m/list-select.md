---
description: "Learn more about: List.Select"
title: "List.Select"
ms.date: 3/9/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Select

## Syntax

<pre>
List.Select(<b>list</b> as list, <b>selection</b> as function) as list
</pre>
  
## About

Returns a list of values from the list `list`, that match the selection condition `selection`.

## Example 1

Find the values in the list {1, -3, 4, 9, -2} that are greater than 0.

**Usage**

```powerquery-m
List.Select({1, -3, 4, 9, -2}, each _ > 0)
```

**Output**

`{1, 4, 9}`
