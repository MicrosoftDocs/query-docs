---
title: "Table.IsEmpty | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.IsEmpty

## Syntax

<pre>
Table.IsEmpty(<b>table</b> as table) as logical 
</pre>
  
## About  
Indicates whether the `table` contains any rows. Returns `true` if there are no rows (i.e. the table is empty), `false` otherwise.

## Example 1
Determine if the table is empty.

```powerquery-m
Table.IsEmpty(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    })
)
```

`false`

## Example 2
Determine if the table `({})` is empty.

```powerquery-m
Table.IsEmpty(Table.FromRecords({}))
```

`true`
