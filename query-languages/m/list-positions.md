---
description: "Learn more about: List.Positions"
title: "List.Positions"
ms.date: 3/8/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Positions

## Syntax

<pre>
List.Positions(<b>list</b> as list) as list
</pre>
  
## About

Returns a list of offsets for the input list `list`. When using List.Transform to change a list, the list of positions can be used to give the transform access to the position.

## Example 1

Find the offsets of values in the list {1, 2, 3, 4, null, 5}.

**Usage**

```powerquery-m
List.Positions({1, 2, 3, 4, null, 5})
```

**Output**

`{0, 1, 2, 3, 4, 5}`
