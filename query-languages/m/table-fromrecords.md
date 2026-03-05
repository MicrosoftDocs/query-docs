---
description: "Learn more about: Table.FromRecords"
title: "Table.FromRecords"
ms.subservice: m-source
ms.topic: reference
---
# Table.FromRecords

## Syntax

<pre>
Table.FromRecords(
    <b>records</b> as list,
    optional <b>columns</b> as any,
    optional <b>missingField</b> as nullable number
) as table
</pre>

## About

Converts a specified list of records into a table.

* `records`: The list of records to convert to a table.
* `columns`: (Optional) A list of the table's column names, or the table's type.
* `missingField`: (Optional) Specifies how to handle missing fields in a row. Use one of the following values:
  * `MissingField.Error`: Any missing fields produce an error (default).
  * `MissingField.UseNull`: Any missing fields are included as `null` values.

  Using `MissingField.Ignore` in this parameter produces an error.

## Example 1

Create a table from records, using record field names as column names.

**Usage**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```

**Output**

```powerquery-m
#table(type table[CustomerID = any, Name = any, Phone = any],
{
    {1, "Bob", "123-4567"},
    {2, "Jim", "987-6543"},
    {3, "Paul", "543-7890"}
})
```

## Example 2

Create a table from records with typed columns and select the number columns.

**Usage**

```powerquery-m
Table.ColumnsOfType(
    Table.FromRecords(
        {[CustomerID = 1, Name = "Bob"]},
        type table[CustomerID = Number.Type, Name = Text.Type]
    ),
    {type number}
)
```

**Output**

`{"CustomerID"}`

## Example 3

Create a table containing the first name, middle initial, and last name of the customers from the specified records. If any of the values are missing, replace the value with `null`.

**Usage**

```powerquery-m
Table.FromRecords({
        [CustomerID = 1, FirstName = "Bob", MiddleInitial = "C", LastName = "Smith"],
        [CustomerID = 2, FirstName = "Sarah", LastName = "Jones"],
        [CustomerID = 3, FirstName = "Harry", MiddleInitial = "H"]
    },
    type table [FirstName = nullable text, MiddleInitial = nullable text, LastName = nullable text],
    MissingField.UseNull)
```

**Output**

```powerquery-m
#table(type table[FirstName = text, MiddleInitial = text, LastName = text],
{
    {"Bob", "C", "Smith"},
    {"Sarah", null, "Jones"},
    {"Harry", "H", null}
})
```

## Related content

[Missing field](missingfield-type.md)
