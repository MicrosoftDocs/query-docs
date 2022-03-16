---
description: "Learn more about: Table.ReplaceErrorValues"
title: "Table.ReplaceErrorValues | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.ReplaceErrorValues

## Syntax

<pre>
Table.ReplaceErrorValues(<b>table</b> as table, <b>errorReplacement</b> as list) as table
</pre>
  
## About

Replaces the error values in the specified columns of the `table` with the new values in the `errorReplacement` list. The format of the list is {{column1, value1}, ...}. There may only be one replacement value per column, specifying the column more than once will result in an error.

## Example 1

Replace the error value with the text "world" in the table.

**Usage**

```powerquery-m
Table.ReplaceErrorValues(
    Table.FromRows({{1, "hello"}, {3, ...}}, {"A", "B"}),
    {"B", "world"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = 1, B = "hello"],
    [A = 3, B = "world"]
})
```

## Example 2

Replace the error value in column A with the text "hello" and in column B with the text "world" in the table.

**Usage**

```powerquery-m
Table.ReplaceErrorValues(
    Table.FromRows({{..., ...}, {1, 2}}, {"A", "B"}),
    {{"A", "hello"}, {"B", "world"}}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = "hello", B = "world"],
    [A = 1, B = 2]
})
```
