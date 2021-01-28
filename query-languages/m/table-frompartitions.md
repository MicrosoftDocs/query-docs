---
description: "Learn more about: Table.FromPartitions"
title: "Table.FromPartitions | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

<table> <tr> <th>Foo</th> <th>Day</th> <th>Month</th> <th>Year</th> </tr> <tr> <td>Bar</td> <td>1</td> <td>Jan</td> <td>1994</td> </tr> <tr> <td>Bar</td> <td>2</td> <td>Jan</td> <td>1994</td> </tr> <tr> <td>Bar</td> <td>3</td> <td>Feb</td> <td>1994</td> </tr> <tr> <td>Bar</td> <td>4</td> <td>Feb</td> <td>1994</td> </tr> </table>
