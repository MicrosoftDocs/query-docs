---
description: "Learn more about: List.Repeat"
title: "List.Repeat | Microsoft Docs"
ms.date: 3/9/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Repeat

## Syntax

<pre>
List.Repeat(<b>list</b> as list, <b>count</b> as number) as list
</pre>
  
## About

Returns a list that is `count` repetitions of the original list, `list`.

## Example 1

Create a list that has {1, 2} repeated 3 times.

**Usage**

```powerquery-m
List.Repeat({1, 2}, 3)
```

**Output**

`{1, 2, 1, 2, 1, 2}`
