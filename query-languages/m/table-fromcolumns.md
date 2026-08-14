---
description: "Learn more about: Table.FromColumns"
title: "Table.FromColumns"
ms.subservice: m-source
ms.topic: reference
---

# Table.FromColumns

## Syntax

<pre>
Table.FromColumns(<b>lists</b> as list, optional <b>columns</b> as any) as table
</pre>

## About

Creates a table of type `columns` from a list `lists` containing nested lists with the column names and values. If some columns have more values than others, the missing values will be filled with the default value, 'null', if the columns are nullable.

## Example 1

Return a table from a list of customer columns.

**Usage**

```powerquery-m
Table.FromColumns({
    {1, 2, 3},
    {"Bob", "Jim", "Paul"},
    {"123-4567", "987-6543", "543-7890"}
})
```

**Output**

```powerquery-m
Table.FromRecords({
    [Column1 = 1, Column2 = "Bob", Column3 = "123-4567"],
    [Column1 = 2, Column2 = "Jim", Column3 = "987-6543"],
    [Column1 = 3, Column2 = "Paul", Column3 = "543-7890"]
})
```

## Example 2

Create a table from a list of customer columns and a list of column names.

**Usage**

```powerquery-m
Table.FromColumns(
    {
      {1, 2, 3},
      {"Bob", "Jim", "Paul"},
      {"123-4567", "987-6543", "543-7890"}
    },
    {"CustomerID", "Name", "Phone"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```

## Example 3

Create a table with different number of columns per row. The missing row value is null.

**Usage**

```powerquery-m
Table.FromColumns(
    {
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    },
    {"column1", "column2", "column3"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [column1 = 1, column2 = 4, column3 = 6],
    [column1 = 2, column2 = 5, column3 = 7],
    [column1 = 3, column2 = null, column3 = 8],
    [column1 = null, column2 = null, column3 = 9]
})
```
