---
description: "Learn more about: Table.FromPartitions"
title: "Table.FromPartitions"
ms.date: 3/10/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.FromPartitions

## Syntax

<pre>
Table.FromPartitions(<b>partitionColumn</b> as text, <b>partitions</b> as list, optional <b>partitionColumnType</b> as nullable type) as table
</pre>
  
## About

Returns a table that is the result of combining a set of partitioned tables, `partitions`. `partitionColumn` is the name of the column to add. The type of the column defaults to `any`, but can be specified by `partitionColumnType`.

## Example 1

Find item type from the list `{number}`.

**Usage**

```powerquery-m
Table.FromPartitions(
    "Year",
    {
        {
            1994,
            Table.FromPartitions(
                "Month",
                {
                    {
                        "Jan",
                        Table.FromPartitions(
                            "Day",
                            {
                                {1, #table({"Foo"}, {{"Bar"}})},
                                {2, #table({"Foo"}, {{"Bar"}})}
                            }
                        )
                    },
                    {
                        "Feb",
                        Table.FromPartitions(
                            "Day",
                            {
                                {3, #table({"Foo"}, {{"Bar"}})},
                                {4, #table({"Foo"}, {{"Bar"}})}
                            }
                        )
                    }
                }
            )
        }
    }
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [
        Foo = "Bar",
        Day = 1,
        Month = "Jan",
        Year = 1994
    ],
    [
        Foo = "Bar",
        Day = 2,
        Month = "Jan",
        Year = 1994
    ],
    [
        Foo = "Bar",
        Day = 3,
        Month = "Feb",
        Year = 1994
    ],
    [
        Foo = "Bar",
        Day = 4,
        Month = "Feb",
        Year = 1994
    ]
})
```
