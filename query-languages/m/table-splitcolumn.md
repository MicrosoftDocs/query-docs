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

Splits the specified column into a set of additional columns using the specified splitter function.

* **table**: The table containing the column to split.
* **sourceColumn**: The name of the column to split.
* **splitter**: The [splitter function](splitter-functions.md) used to split the column (for example, [Splitter.SplitTextByDelimiter](splitter-splittextbydelimiter.md) or [Splitter.SplitTextByPosition](splitter-splittextbyposition.md)).
* **columnNamesOrNumber**: Either a list of new column names to create, or the number of new columns.
* **default**: Overrides the value used when there aren't enough split values to fill all of the new columns. The default for this parameter is `null`.
* **extraColumns**: Specifies what to do if there might be more split values than the number of new columns. You can pass an [ExtraValues.Type](extravalues-type.md) enumeration value to this parameter. The default is `ExtraValues.Ignore`.

## Example 1

Split the name column into first name and last name.

**Usage**

```powerquery-m
let
    Source = #table(type table[CustomerID = number, Name = text, Phone = text],
    {
        {1, "Bob White", "123-4567"},
        {2, "Jim Smith", "987-6543"},
        {3, "Paul", "543-7890"},
        {4, "Cristina Best", "232-1550"}
    }),
    SplitColumns = Table.SplitColumn(
        Source,
        "Name",
        Splitter.SplitTextByDelimiter(" "))
in
    SplitColumns
```

**Output**

```powerquery-m
#table(type table[CustomerID = number, Name.1 = text, Name.2 = text, Phone = text],
{
    {1, "Bob", "White", "123-4567"},
    {2, "Jim", "Smith", "987-6543"},
    {3, "Paul", null, "543-7890"},
    {4, "Cristina", "Best", "232-1550"}
})
```

## Example 2

Split the name column into first name and last name, then rename the new columns.

**Usage**

```powerquery-m
let
    Source = #table(type table[CustomerID = number, Name = text, Phone = text],
    {
        {1, "Bob White", "123-4567"},
        {2, "Jim Smith", "987-6543"},
        {3, "Paul", "543-7890"},
        {4, "Cristina Best", "232-1550"}
    }),
    SplitColumns = Table.SplitColumn(
        Source,
        "Name",
        Splitter.SplitTextByDelimiter(" "),
        {"First Name", "Last Name"})
in
    SplitColumns
```

**Output**

```powerquery-m
#table(type table[CustomerID = number, First Name = text, Last Name = text, Phone = text],
{
    {1, "Bob", "White", "123-4567"},
    {2, "Jim", "Smith", "987-6543"},
    {3, "Paul", null, "543-7890"},
    {4, "Cristina", "Best", "232-1550"}
})
```

## Example 3

Split the name column into first name and last name, rename the new columns, and fill in any blanks with "-No Entry-".

**Usage**

```powerquery-m
let
    Source = #table(type table[CustomerID = number, Name = text, Phone = text],
    {
        {1, "Bob White", "123-4567"},
        {2, "Jim Smith", "987-6543"},
        {3, "Paul", "543-7890"},
        {4, "Cristina Best", "232-1550"}
    }),
    SplitColumns = Table.SplitColumn(
        Source,
        "Name",
        Splitter.SplitTextByDelimiter(" "),
        {"First Name", "Last Name"},
        "-No Entry-")
in
    SplitColumns
```

**Output**

```powerquery-m
#table(type table[CustomerID = number, First Name = text, Last Name = text, Phone = text],
{
    {1, "Bob", "White", "123-4567"},
    {2, "Jim", "Smith", "987-6543"},
    {3, "Paul", "-No Entry-", "543-7890"},
    {4, "Cristina", "Best", "232-1550"}
})
```

## Example 4

Split the name column into first name and last name, then rename the new columns. Because there might be more values than the number of available columns, make the last name column a list that includes all values after the first name.

**Usage**

```powerquery-m
let
    Source = #table(type table[CustomerID = number, Name = text, Phone = text],
    {
        {1, "Bob White", "123-4567"},
        {2, "Jim Smith", "987-6543"},
        {3, "Paul Green", "543-7890"},
        {4, "Cristina J. Best", "232-1550"}
    }),
    SplitColumns = Table.SplitColumn(
        Source,
        "Name",
        Splitter.SplitTextByDelimiter(" "),
        {"First Name", "Last Name"},
        null,
        ExtraValues.List)
in
    SplitColumns
```

**Output**

```powerquery-m
#table(type table[CustomerID = number, First Name = text, Last Name = text, Phone = text],
{
    {1, "Bob", {"White"}, "123-4567"},
    {2, "Jim", {"Smith"}, "987-6543"},
    {3, "Paul", {"Green"}, "543-7890"},
    {4, "Cristina", {"J.", "Best"}, "232-1550"}
})
```
