---
description: "Learn more about: Table.ExpandListColumn"
title: "Table.ExpandListColumn"
ms.subservice: m-source
---
# Table.ExpandListColumn

## Syntax

<pre>
Table.ExpandListColumn(<b>table</b> as table, <b>column</b> as text) as table
</pre>
  
## About

Given a `table` where `column` contains a list of values, splits the list into a row for each value. Values in the other columns are duplicated in each new row created. This function can also expand nested tables by treating them as lists of records.

## Example 1

Split the list column [Name].

**Usage**

```powerquery-m
Table.ExpandListColumn(
    Table.FromRecords({[Name = {"Bob", "Jim", "Paul"}, Discount = .15]}),
    "Name"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Name = "Bob", Discount = 0.15],
    [Name = "Jim", Discount = 0.15],
    [Name = "Paul", Discount = 0.15]
})
```

## Example 2

Split the nested table column [Components].

**Usage**

```powerquery-m
Table.ExpandListColumn(
    #table(
        {"Part", "Components"},
        {
            {"Tool", #table({"Name", "Quantity"}, {{"Thingamajig", 2}, {"Widget", 3}})}
        }
    ),
    "Components"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Part = "Tool", Components = [Name = "Thingamajig", Quantity = 2]],
    [Part = "Tool", Components = [Name = "Widget", Quantity = 3]]
})
```
