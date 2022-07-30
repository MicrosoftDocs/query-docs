---
description: "Learn more about: Table.StopFolding"
title: "Table.StopFolding"
ms.date: 4/13/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.StopFolding

## Syntax

<pre>
Table.StopFolding(<b>table</b> as table) as table
</pre>

## About

Prevents any downstream operations from being run against the original source of the data in `table`.

## Example 1

Fetches data from a SQL table in a way that prevents any downstream operations from running as a query on the SQL server.

**Usage**

```powerquery-m
let
    Source = Sql.Database("SomeSQLServer", "MyDb"),
    MyTable = Source{[Item="MyTable"]}[Data],
    MyLocalTable = Table.StopFolding(dbo_MyTable)
in
    MyLocalTable
```

**Output**

`table`
