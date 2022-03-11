---
description: "Learn more about: Table.FromValue"
title: "Table.FromValue | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.FromValue

## Syntax

<pre>
Table.FromValue(<b>value</b> as any, optional <b>options</b> as nullable record) as table  
</pre>
  
## About

Creates a table with a column containing the provided value or list of values, `value`. An optional record parameter, `options`, may be specified to control the following options:

* `DefaultColumnName`: The column name used when constructing a table from a list or scalar value.

## Example 1

Create a table from the value 1.

**Usage**

```powerquery-m
Table.FromValue(1)
```

**Output**

`Table.FromRecords({[Value = 1]})`

## Example 2

Create a table from the list.

**Usage**

```powerquery-m
Table.FromValue({1, "Bob", "123-4567"})
```

**Output**

```powerquery-m
Table.FromRecords({
    [Value = 1],
    [Value = "Bob"],
    [Value = "123-4567"]
})
```

## Example 3

Create a table from the value 1, with a custom column name.

**Usage**

```powerquery-m
Table.FromValue(1, [DefaultColumnName = "MyValue"])
```

**Output**

`Table.FromRecords({[MyValue = 1]})`
