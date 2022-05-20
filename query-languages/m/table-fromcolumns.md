---
description: "Learn more about: Table.FromColumns"
title: "Table.FromColumns | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.FromColumns

## Syntax

<pre>
Table.FromColumns(<b>lists</b> as list, optional <b>columns</b> as any) as table
</pre>
  
## About

Creates a table of type `columns` from a list `lists` containing nested lists with the column names and values. If some columns have more values then others, the missing values will be filled with the default value, 'null', if the columns are nullable.

## Example 1

Return a table from a list of customer names in a list. Each value in the customer list item becomes a row value, and each list becomes a column.

**Usage**

```powerquery-m
Table.FromColumns({
    {1, "Bob", "123-4567"},
    {2, "Jim", "987-6543"},
    {3, "Paul", "543-7890"}
})
```

**Output**

```powerquery-m
Table.FromRecords({
    [Column1 = 1, Column2 = 2, Column3 = 3],
    [Column1 = "Bob", Column2 = "Jim", Column3 = "Paul"],
    [Column1 = "123-4567", Column2 = "987-6543", Column3 = "543-7890"]
})
```

## Example 2

Create a table from a given list of columns and a list of column names.

**Usage**

```powerquery-m
Table.FromColumns(
    {
        {1, "Bob", "123-4567"},
        {2, "Jim", "987-6543"},
        {3, "Paul", "543-7890"}
    },
    {"CustomerID", "Name", "Phone"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = 2, Phone = 3],
    [CustomerID = "Bob", Name = "Jim", Phone = "Paul"],
    [CustomerID = "123-4567", Name = "987-6543", Phone = "543-7890"]
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
