---
description: "Learn more about: List.SingleOrDefault"
title: "List.SingleOrDefault"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.SingleOrDefault

## Syntax

<pre>
List.SingleOrDefault(<b>list</b> as list, optional <b>default</b> as any) as any 
</pre>
  
## About

If there is only one item in the list `list`, returns that item. If the list is empty, the function returns null unless an optional `default` is specified. If there is more than one item in the list, the function returns an error.

## Example 1

Find the single value in the list {1}.

**Usage**

```powerquery-m
List.SingleOrDefault({1})
```

**Output**

`1`

## Example 2

Find the single value in the list {}.

**Usage**

```powerquery-m
List.SingleOrDefault({})
```

**Output**

`null`

## Example 3

Find the single value in the list {}. If is empty, return -1.

**Usage**

```powerquery-m
List.SingleOrDefault({}, -1)
```

**Output**

`-1`
