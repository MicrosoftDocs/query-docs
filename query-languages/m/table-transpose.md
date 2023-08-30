---
description: "Learn more about: Table.Transpose"
title: "Table.Transpose"
---
# Table.Transpose

## Syntax

<pre>
Table.Transpose(<b>table</b> as table, optional <b>columns</b> as any) as table
</pre>
  
## About

Makes columns into rows and rows into columns.

## Example 1

Make the rows of the table of name-value pairs into columns.

**Usage**

```powerquery-m
Table.Transpose(
    Table.FromRecords({
        [Name = "Full Name", Value = "Fred"],
        [Name = "Age", Value = 42],
        [Name = "Country", Value = "UK"]
    })
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Column1 = "Full Name", Column2 = "Age", Column3 = "Country"],
    [Column1 = "Fred", Column2 = 42, Column3 = "UK"]
})
```
