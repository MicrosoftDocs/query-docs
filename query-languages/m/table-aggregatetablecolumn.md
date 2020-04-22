---
title: "Table.AggregateTableColumn | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.AggregateTableColumn

## Syntax

<pre>
Table.AggregateTableColumn(<b>table</b> as table, <b>column</b> as text, <b>aggregations</b> as list) as table
</pre>
  
## About  
Aggregates tables in `table`[`column`] into multiple columns containing aggregate values for the tables. `aggregations` is used to specify the columns containing the tables to aggregate, the aggregation functions to apply to the tables to generate their values, and the names of the aggregate columns to create.

## Example 1
Aggregate table columns in `[t]` in the table `{[t = {[a=1, b=2, c=3], [a=2,b=4,c=6]}, b = 2]}` into the sum of `[t.a]`, the min and max of `[t.b]`, and the count of values in `[t.a]`.

```powerquery-m
Table.AggregateTableColumn( 
    Table.FromRecords( 
        { 
            [ 
                t = Table.FromRecords({ 
                    [a = 1, b = 2, c = 3], 
                    [a = 2,b = 4,c = 6] 
                }), 
                b = 2 
            ] 
        }, 
        type table [t = table [a = number, b = number, c = number], b = number] 
    ), 
    "t", 
    { 
        {"a", List.Sum, "sum of t.a"}, 
        {"b", List.Min, "min of t.b"}, 
        {"b", List.Max, "max of t.b"}, 
        {"a", List.Count, "count of t.a"} 
    } 
)
```

<table> <tr> <th>sum of t.a</th> <th>min of t.b</th> <th>max of t.b</th> <th>count of t.a</th> <th>b</th> </tr> <tr> <td>3</td> <td>2</td> <td>4</td> <td>2</td> <td>2</td> </tr> </table>
