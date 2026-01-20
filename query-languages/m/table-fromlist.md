---
description: "Learn more about: Table.FromList"
title: "Table.FromList"
ms.subservice: m-source
ms.topic: reference
---
# Table.FromList

## Syntax

<pre>
Table.FromList(
    <b>list</b> as list,
    optional <b>splitter</b> as nullable function,
    optional <b>columns</b> as any,
    optional <b>default</b> as any,
    optional <b>extraValues</b> as nullable number
) as table
</pre>
  
## About

Converts a list, `list` into a table by applying the optional [splitting function](splitter-functions.md), `splitter`, to each item in the list. By default, the list is assumed to be a list of text values that is split by commas. Optional `columns` may be the number of columns, a list of columns or a TableType. Optional `default` and `extraValues` may also be specified.

## Example 1

Create a table from a list using the default splitter.

**Usage**

```powerquery-m
Table.FromList(
    {"a,apple", "b,ball", "c,cookie", "d,door"},
    null,
    {"Letter", "Example Word"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Letter = "a", #"Example Word" = "apple"],
    [Letter = "b", #"Example Word" = "ball"],
    [Letter = "c", #"Example Word" = "cookie"],
    [Letter = "d", #"Example Word" = "door"]
})
```

## Example 2

Create a table from a list using a custom splitter.

**Usage**

```powerquery-m
Table.FromList(
    {"a,apple", "b,ball", "c,cookie", "d,door"},
    Splitter.SplitByNothing(),
    {"Letter and Example Word"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [#"Letter and Example Word" = "a,apple"],
    [#"Letter and Example Word" = "b,ball"],
    [#"Letter and Example Word" = "c,cookie"],
    [#"Letter and Example Word" = "d,door"]
})
```

## Example 3

Create a table from the list using the [Record.FieldValues](record-fieldvalues.md) splitter.

**Usage**

```powerquery-m
Table.FromList(
    {
        [CustomerID = 1, Name = "Bob"],
        [CustomerID = 2, Name = "Jim"]
    },
    Record.FieldValues,
    {"CustomerID", "Name"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob"],
    [CustomerID = 2, Name = "Jim"]
})
```
