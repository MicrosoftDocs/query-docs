---
description: "Learn more about: Table.Repeat"
title: "Table.Repeat"
ms.date: 3/10/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.Repeat

## Syntax

<pre>
Table.Repeat(<b>table</b> as table, <b>count</b> as number) as table  
</pre>
  
## About

Returns a table with the rows from the input `table` repeated the specified `count` times.

## Example 1

Repeat the rows in the table two times.

**Usage**

```powerquery-m
Table.Repeat(
    Table.FromRecords({
        [a = 1, b = "hello"],
        [a = 3, b = "world"]
    }),
    2

```

**Output**

```powerquery-m
Table.FromRecords({
    [a = 1, b = "hello"],
    [a = 3, b = "world"],
    [a = 1, b = "hello"],
    [a = 3, b = "world"]
})
```
