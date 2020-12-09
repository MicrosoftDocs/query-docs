---
title: "Table.AddKey | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.AddKey

## Syntax

<pre>
Table.AddKey(<b>table</b> as table, <b>columns</b> as list, <b>isPrimary</b> as logical) as table
</pre>
  
## About  
Add a key to `table`, given `columns` is the subset of `table`'s column names that defines the key, and `isPrimary` specifies whether the key is primary.

## Example 1
Add a key to {[Id = 1, Name = "Hello There"], [Id = 2, Name = "Good Bye"]} that comprise of {"Id"} and make it a primary.

```powerquery-m
let
    tableType = type table [Id = Int32.Type, Name = text],
    table = Table.FromRecords({
        [Id = 1, Name = "Hello There"],
        [Id = 2, Name = "Good Bye"]
    }),
    resultTable = Table.AddKey(table, {"Id"}, true)
in
    resultTable
```

<table> <tr> <th>Id</th> <th>Name</th> </tr> <tr> <td>1</td> <td>Hello There</td> </tr> <tr> <td>2</td> <td>Good Bye</td> </tr> </table>
