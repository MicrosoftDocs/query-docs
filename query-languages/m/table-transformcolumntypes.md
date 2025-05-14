---
description: "Learn more about: Table.TransformColumnTypes"
title: "Table.TransformColumnTypes"
ms.subservice: m-source
---
# Table.TransformColumnTypes

## Syntax

<pre>
Table.TransformColumnTypes(<b>table</b> as table, <b>typeTransformations</b> as list, optional <b>culture</b> as nullable text) as table
</pre>
  
## About

Returns a table by applying the transform operations to the specified columns using an optional culture.

* `table`: The input table to transform.
* `typeTransformations`: The type transformations to apply. The format for a single transformation is { column name, type value }. A list of transformations can be used to change the types of more than one column at a time. If a column doesn't exist, an error is raised.
* `culture`: (Optional) The culture to use when transforming the column types (for example, "en-US"). If a record is specified for `culture`, it can contain the following fields:
  * `Culture`: The culture to use when transforming the column types (for example, "en-US").
  * `MissingField`: If a column doesn't exist, an error is raised unless this field provides an alternative behavior (for example, [MissingField.UseNull](missingfield-type.md) or [MissingField.Ignore](missingfield-type.md)).

The type value in the `typeTransformations` parameter can be `any`, all of the `number` types, `text`, all of the `date`, `time`, `datetime`, `datetimezone`, and `duration` types, `logical`, or `binary`. The `list`, `record`, `table`, or `function` types aren't valid for this parameter.

For each column listed in `typeTransformations`, the ".From" method corresponding to the specified type value is normally used to perform the transformation. For example, if a [Currency.Type](type-conversion.md#commonly-used-types) type value is given for a column, the transformation function [Currency.From](currency-from.md) is applied to each value in that column.

## Example 1

Transform the number values in the first column to text values.

**Usage**

```powerquery-m
let
    Source = #table(type table [a = number, b = number],
    {
        {1, 2},
        {3, 4}
    }),
    #"Transform Column" = Table.TransformColumnTypes(
        Source, 
        {"a", type text}
    )
in
    #"Transform Column"
```

**Output**

```powerquery-m
#table(type table [a = text, b = number],
{
    {"1", 2},
    {"3", 4}
})
```

## Example 2

Transform the dates in the table to their French text equivalents.

**Usage**

```powerquery-m
let
    Source = #table(type table [Company ID = text, Country = text, Date = date],
    {
        {"JS-464", "USA", #date(2024, 3, 24)},
        {"LT-331", "France", #date(2024, 10, 5)},
        {"XE-100", "USA", #date(2024, 5, 21)},
        {"RT-430", "Germany", #date(2024, 1,18)},
        {"LS-005", "France", #date(2023, 12, 31)},
        {"UW-220", "Germany", #date(2024, 2, 25)}
    }),
    #"Transform Column" = Table.TransformColumnTypes(
        Source,
        {"Date", type text},
        "fr-FR"
    )
in
    #"Transform Column"
```

**Output**

```powerquery-m
#table(type table [Company ID = text, Country = text, Date = text],
    {
        {"JS-464", "USA", "24/03/2024"},
        {"LT-331", "France", "05/10/2024"},
        {"XE-100", "USA", "21/05/2024"},
        {"RT-430", "Germany", "18/01/2024"},
        {"LS-005", "France", "31/12/2023"},
        {"UW-220", "Germany", "25/02/2024"}
    })
```

## Example 3

Transform the dates in the table to their German text equivalents, and the values in the table to percentages.

**Usage**

```powerquery-m
let
    Source = #table(type table [Date = date, Customer ID = text, Value = number],
    {
        {#date(2024, 3, 12), "134282", .24368},
        {#date(2024, 5, 30), "44343", .03556},
        {#date(2023, 12, 14), "22", .3834}
    }),
    #"Transform Columns" = Table.TransformColumnTypes(
        Source, 
        {{"Date", type text}, {"Value", Percentage.Type}},
        "de-DE") 
in
    #"Transform Columns"
```

**Output**

```powerquery-m
#table(type table [Date = text, Customer ID = text, Value = Percentage.Type],
{
    {"12.03.2024", "134282", .24368},
    {"30.05.2024", "44343", .03556},
    {"14.12.2023", "22", .3834}
})
```
   
## Related content

* [Types and type conversion](type-conversion.md)
* [How culture affects text formatting](how-culture-affects-text-formatting.md)
