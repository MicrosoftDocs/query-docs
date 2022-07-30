---
description: "Learn more about: Table.DemoteHeaders"
title: "Table.DemoteHeaders"
ms.date: 3/10/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.DemoteHeaders

## Syntax

<pre>
Table.DemoteHeaders(<b>table</b> as table) as table
</pre>
  
## About

Demotes the column headers (i.e. column names) to the first row of values. The default column names are "Column1", "Column2" and so on.

## Example 1

Demote the first row of values in the table.

**Usage**

```powerquery-m
Table.DemoteHeaders(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"]
    })
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Column1 = "CustomerID", Column2 = "Name", Column3 = "Phone"],
    [Column1 = 1, Column2 = "Bob", Column3 = "123-4567"],
    [Column1 = 2, Column2 = "Jim", Column3 = "987-6543"]
})
```
