---
description: "Learn more about: Table.SplitColumn"
title: "Table.SplitColumn"
ms.subservice: m-source
---
# Table.SplitColumn

## Syntax

<pre>
Table.SplitColumn(<b>table</b> as table, <b>sourceColumn</b> as text, <b>splitter</b> as function, optional <b>columnNamesOrNumber</b> as any, optional <b>default</b> as any, optional <b>extraColumns</b> as any) as table
</pre>
  
## About

Splits the specified columns into a set of additional columns using the specified splitter function.

## Example 1

Split the [Name] column at position of "i" into two columns

**Usage**

```powerquery-m
let
    Customers = Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Cristina", Phone = "232-1550"]
    })
in
    Table.SplitColumn(Customers, "Name", Splitter.SplitTextByDelimiter("i"), 2)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name.1 = "Bob", Name.2 = null, Phone = "123-4567"],
    [CustomerID = 2, Name.1 = "J", Name.2 = "m", Phone = "987-6543"],
    [CustomerID = 3, Name.1 = "Paul", Name.2 = null, Phone = "543-7890"],
    [CustomerID = 4, Name.1 = "Cr", Name.2 = "st", Phone = "232-1550"]
})
```
