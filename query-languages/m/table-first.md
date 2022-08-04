---
description: "Learn more about: Table.First"
title: "Table.First"
ms.date: 3/10/2022
---
# Table.First

## Syntax

<pre>
Table.First(<b>table</b> as table, optional <b>default</b> as any) as any
</pre>
  
## About

Returns the first row of the `table` or an optional default value, `default`, if the table is empty.

## Example 1

Find the first row of the table.

**Usage**

```powerquery-m
Table.First(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    })
)
```

**Output**

`[CustomerID = 1, Name = "Bob", Phone = "123-4567"]`

## Example 2

Find the first row of the table `({})` or return [a = 0, b = 0] if empty.

**Usage**

```powerquery-m
Table.First(Table.FromRecords({}), [a = 0, b = 0])
```

**Output**

`[a = 0, b = 0]`
