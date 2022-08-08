---
description: "Learn more about: Table.Contains"
title: "Table.Contains"
ms.date: 3/14/2022
---
# Table.Contains

## Syntax

<pre>
Table.Contains(<b>table</b> as table, <b>row</b> as record, optional <b>equationCriteria</b> as any) as logical
</pre>
  
## About

Indicates whether the specified record, `row`, appears as a row in the `table`. An optional parameter `equationCriteria` may be specified to control comparison between the rows of the table.

## Example 1

Determine if the table contains the row.

**Usage**

```powerquery-m
Table.Contains(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    [Name = "Bob"]
)
```

**Output**

`true`

## Example 2

Determine if the table contains the row.

**Usage**

```powerquery-m
Table.Contains(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    [Name = "Ted"]
)
```

**Output**

`false`

## Example 3

Determine if the table contains the row comparing only the column [Name].

**Usage**

```powerquery-m
Table.Contains(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    [CustomerID = 4, Name = "Bob"],
    "Name"
)
```

**Output**

`true`
