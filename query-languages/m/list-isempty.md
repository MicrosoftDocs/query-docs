---
description: "Learn more about: List.IsEmpty"
title: "List.IsEmpty"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.IsEmpty

## Syntax

<pre>
List.IsEmpty(<b>list</b> as list) as logical
</pre>
  
## About

Returns `true` if the list, `list`, contains no values (length 0). If the list contains values (length > 0), returns `false`.

## Example 1

Find if the list {} is empty.

**Usage**

```powerquery-m
List.IsEmpty({})
```

**Output**

`true`

## Example 2

Find if the list {1, 2} is empty.

**Usage**

```powerquery-m
List.IsEmpty({1, 2})
```

**Output**

`false`
