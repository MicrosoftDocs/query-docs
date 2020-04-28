---
title: "Table.Partition | Microsoft Docs"
ms.date: 4/24/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Partition

## Syntax

<pre>  
Table.Partition(<b>table</b> as table, <b>column</b> as text, <b>groups</b> as number, <b>hash</b> as function) as list 
</pre>
  
## About  
Partitions the <code>table</code> into a list of <code>groups</code> number of tables, based on the value of the <code>column</code> and a <code>hash</code> function. The <code>hash</code> function is applied to the value of the <code>column</code> row to obtain a hash value for the row. The hash value modulo <code>groups</code> determines in which of the returned tables the row will be placed. <ul> <li><code>table</code>: The table to partition.</li> <li><code>column</code>: The column to hash to determine which returned table the row is in.</li> <li><code>groups</code>: The number of tables the input table will be partitioned into.</li> <li><code>hash</code>: The function applied to obtain a hash value.</li> </ul>  
  
## Example  

Partition the table <code>({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})</code> into 2 tables on column [a], using the value of the columns as the hash function.

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

```
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