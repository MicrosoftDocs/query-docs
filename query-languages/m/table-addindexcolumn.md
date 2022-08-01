---
description: "Learn more about: Table.AddIndexColumn"
title: "Table.AddIndexColumn"
ms.date: 3/10/2022
---
# Table.AddIndexColumn

## Syntax

<pre>
Table.AddIndexColumn(<b>table</b> as table, <b>newColumnName</b> as text, optional <b>initialValue</b> as nullable number, optional <b>increment</b> as nullable number, optional <b>columnType</b> as nullable type) as table
</pre>
  
## About

Appends a column named `newColumnName` to the `table` with explicit position values. An optional value, `initialValue`, the initial index value. An optional value, `increment`, specifies how much to increment each index value.

## Example 1

Add an index column named "Index" to the table.

**Usage**

```powerquery-m
Table.AddIndexColumn(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "Index"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567", Index = 0],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543", Index = 1],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890", Index = 2],
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550", Index = 3]
})
```

## Example 2

Add an index column named "index", starting at value 10 and incrementing by 5, to the table.

**Usage**

```powerquery-m
Table.AddIndexColumn(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "Index",
    10,
    5
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567", Index = 10],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543", Index = 15],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890", Index = 20],
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550", Index = 25]
})
```
