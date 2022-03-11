---
description: "Learn more about: Table.FromList"
title: "Table.FromList | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.FromList

## Syntax

<pre>
Table.FromList(<b>list</b> as list, optional <b>splitter</b> as nullable function, optional <b>columns</b> as any, optional <b>default</b> as any, optional <b>extraValues</b> as nullable number) as table
</pre>
  
## About

Converts a list, `list` into a table by applying the optional splitting function, `splitter`, to each item in the list. By default, the list is assumed to be a list of text values that is split by commas. Optional `columns` may be the number of columns, a list of columns or a TableType. Optional `default` and `extraValues` may also be specified.

## Example 1

Create a table from the list with the column named "Letters" using the default splitter.

**Usage**

```powerquery-m
Table.FromList({"a", "b", "c", "d"}, null, {"Letters"})
```

**Output**

```powerquery-m
Table.FromRecords({
    [Letters = "a"],
    [Letters = "b"],
    [Letters = "c"],
    [Letters = "d"]
})
```

## Example 2

Create a table from the list using the Record.FieldValues splitter with the resulting table having "CustomerID" and "Name" as column names.

**Usage**

```powerquery-m
Table.FromList(
    {
        [CustomerID = 1, Name = "Bob"],
        [CustomerID = 2, Name = "Jim"]
    },
    Record.FieldValues,
    {"CustomerID", "Name"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob"],
    [CustomerID = 2, Name = "Jim"]
})
```
