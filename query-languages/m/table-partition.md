---
description: "Learn more about: Table.Partition"
title: "Table.Partition"
ms.subservice: m-source
ms.topic: reference
---
# Table.Partition

## Syntax

<pre>  
Table.Partition(
    <b>table</b> as table,
    <b>column</b> as text,
    <b>groups</b> as number,
    <b>hash</b> as function
) as list
</pre>
  
## About

Partitions the `table` into a list of `groups` number of tables, based on the value of the `column` and a `hash` function. The `hash` function is applied to the value of the `column` row to obtain a hash value for the row. The hash value modulo `groups` determines in which of the returned tables the row will be placed.

* `table`: The table to partition.
* `column`: The column to hash to determine which returned table the row is in.
* `groups`: The number of tables the input table will be partitioned into.
* `hash`: The function applied to obtain a hash value.  
  
## Example 1

Partition the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})` into 2 tables on column [a], using the value of the columns as the hash function.

**Usage**

```powerquery-m
Table.Partition(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 1, b = 4],
        [a = 2, b = 4],
        [a = 1, b = 4]
    }),
    "a",
    2,
    each _
)
```

**Output**

```powerquery-m
{
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 2, b = 4]
    }),
    Table.FromRecords({
        [a = 1, b = 4],
        [a = 1, b = 4]
    })
}
```
