---
description: "Learn more about: Table.ExpandListColumn"
title: "Table.ExpandListColumn"
---
# Table.ExpandListColumn

## Syntax

<pre>
Table.ExpandListColumn(<b>table</b> as table, <b>column</b> as text) as table
</pre>
  
## About

Given a `table`, when `column` contains a list of values, splits the list into a row for each value. If, instead, `column` contains a nested table, treats the nested table as though it were a list of records, which it then splits into a row for each value. Values in the other columns are duplicated in each new row created.

## Example 1

Split the list column [Name] in the table.

**Usage**

```powerquery-m
Table.ExpandListColumn(
    Table.FromRecords({[Name = {"Bob", "Jim", "Paul"}, Discount = .15]}),
    "Name"
)
```

## Example 1

Split the nested table column [Components] in the table.

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
    [Part = "Tool", [Name = "Thingamajig", Quantity = 2],
    [Part = "Tool", [Name = "Widget", Quantity = 3]
})
```
