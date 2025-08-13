---
description: "Learn more about: Table.TransformColumnNames"
title: "Table.TransformColumnNames"
ms.subservice: m-source
---
# Table.TransformColumnNames

## Syntax

<pre>
Table.TransformColumnNames(
    <b>table</b> as table,
    <b>nameGenerator</b> as function,
    optional <b>options</b> as nullable record
) as table
</pre>
  
## About

Transforms column names by using the given `nameGenerator` function. Valid options:

`MaxLength` specifies the maximum length of new column names. If the given function results with a longer column name, the long name will be trimmed.

`Comparer` is used to control the comparison while generating new column names. Comparers can be used to provide case-insensitive or culture and locale-aware comparisons.

The following built-in comparers are available in the formula language:

* `Comparer.Ordinal`: Used to perform an exact ordinal comparison
* `Comparer.OrdinalIgnoreCase`: Used to perform an exact ordinal case-insensitive comparison
* `Comparer.FromCulture`: Used to perform a culture-aware comparison

## Example 1

Remove the `#(tab)` character from column names

**Usage**

```powerquery-m
Table.TransformColumnNames(Table.FromRecords({[#"Col#(tab)umn" = 1]}), Text.Clean)
```

**Output**

`Table.FromRecords({[Column = 1]})`

## Example 2

Transform column names to generate case-insensitive names of length 6.

**Usage**

```powerquery-m
Table.TransformColumnNames(
    Table.FromRecords({[ColumnNum = 1, cOlumnnum = 2, coLumnNUM = 3]}),
    Text.Clean,
    [MaxLength = 6, Comparer = Comparer.OrdinalIgnoreCase]
)
```

**Output**

`Table.FromRecords({[Column = 1, cOlum1 = 2, coLum2 = 3]})`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
