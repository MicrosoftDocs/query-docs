---
description: "Learn more about: List.First"
title: "List.First | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.First

## Syntax

<pre>
List.First(<b>list</b> as list, optional <b>defaultValue</b> as any) as any
</pre>
  
## About

Returns the first item in the list `list`, or the optional default value, `defaultValue`, if the list is empty. If the list is empty and a default value is not specified, the function returns `null`.

## Example 1

Find the first value in the list {1, 2, 3}.

**Usage**

```powerquery-m
List.First({1, 2, 3})
```

**Output**

`1`

## Example 2

Find the first value in the list {}. If the list is empty, return -1.

**Usage**

```powerquery-m
List.First({}, -1)
```

**Output**

`-1`
