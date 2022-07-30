---
description: "Learn more about: Table.IsEmpty"
title: "Table.IsEmpty"
ms.date: 3/14/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Table.IsEmpty(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    })
)
```

**Output**

`false`

## Example 2

Determine if the table `({})` is empty.

**Usage**

```powerquery-m
Table.IsEmpty(Table.FromRecords({}))
```

**Output**

`true`
