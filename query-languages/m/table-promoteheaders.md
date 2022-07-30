---
description: "Learn more about: Table.PromoteHeaders"
title: "Table.PromoteHeaders"
ms.date: 3/10/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.PromoteHeaders

## Syntax

<pre>
Table.PromoteHeaders(<b>table</b> as table, optional <b>options</b> as nullable record) as table
</pre>

## About

Promotes the first row of values as the new column headers (i.e. column names). By default, only text or number values are promoted to headers. Valid options:

* `PromoteAllScalars`: If set to `true`, all the scalar values in the first row are promoted to headers using the `Culture`, if specified (or current document locale). For values that cannot be converted to text, a default column name will be used.
* `Culture`: A culture name specifying the culture for the data.

## Example 1

Promote the first row of values in the table.

**Usage**

```powerquery-m
Table.PromoteHeaders(
    Table.FromRecords({
        [Column1 = "CustomerID", Column2 = "Name", Column3 = #date(1980, 1, 1)],
        [Column1 = 1, Column2 = "Bob", Column3 = #date(1980, 1, 1)]
    })
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob", Column3 = #date(1980, 1, 1)]})`

## Example 2

Promote all the scalars in the first row of the table to headers.

**Usage**

```powerquery-m
Table.PromoteHeaders(
    Table.FromRecords({
        [Rank = 1, Name = "Name", Date = #date(1980, 1, 1)],
        [Rank = 1, Name = "Bob", Date = #date(1980, 1, 1)]}
    ),
    [PromoteAllScalars = true, Culture = "en-US"]
)
```

**Output**

`Table.FromRecords({[1 = 1, Name = "Bob", #"1/1/1980" = #date(1980, 1, 1)]})`
