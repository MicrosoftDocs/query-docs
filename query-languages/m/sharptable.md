---
description: "Learn more about: #table"
title: "#table"
ms.subservice: m-source
ms.topic: reference
---
# #table

## Syntax

<pre>
#table(<b>columns</b> as any, <b>rows</b> as any) as any
</pre>

## About

Creates a table value from `columns` and `rows`. The `columns` value can be a list of column names, a table type, a number of columns, or null. The `rows` value is a list of lists, where each element contains the column values for a single row.

## Example 1

Create an empty table.

**Usage**

```powerquery-m
#table({}, {})
```

**Output**

```powerquery-m
#table({}, {})
```

## Example 2

Create a table by inferring the number of columns from the first row.

**Usage**

```powerquery-m
#table(null, {{"Betty", 90.3}, {"Carl", 89.5}})
```

**Output**

```powerquery-m
#table({"Column1", "Column2"}, {{"Betty", 90.3}, {"Carl", 89.5}})
```

## Example 3

Create a table by specifying the number of columns.

**Usage**

```powerquery-m
#table(2, {{"Betty", 90.3}, {"Carl", 89.5}})
```

**Output**

```powerquery-m
#table({"Column1", "Column2"}, {{"Betty", 90.3}, {"Carl", 89.5}})
```

## Example 4

Create a table by providing a list of column names.

**Usage**

```powerquery-m
#table({"Name", "Score"}, {{"Betty", 90.3}, {"Carl", 89.5}})
```

**Output**

```powerquery-m
#table({"Name", "Score"}, {{"Betty", 90.3}, {"Carl", 89.5}})
```

## Example 5

Create a table with an explicit type.

**Usage**

```powerquery-m
#table(type table [Name = text, Score = number], {{"Betty", 90.3}, {"Carl", 89.5}})
```

**Output**

```powerquery-m
#table(type table [Name = text, Score = number], {{"Betty", 90.3}, {"Carl", 89.5}})
```

## Related content

* [Types and type conversion](type-conversion.md)
