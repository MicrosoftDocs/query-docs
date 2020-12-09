---
title: "Table.ToRows | Microsoft Docs"
ms.date: 4/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.ToRows

## Syntax

<pre>
Table.ToRows(<b>table</b> as table) as list 
</pre>
  
## About  
Creates a list of nested lists from the table, <code>table</code>. Each list item is an inner list that contains the row values.  
  
  
## Example  

Create a list of the row values from the table.

```powerquery-m
Table.ToRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    })
)
```

<table> <tr><td>[List]</td></tr> <tr><td>[List]</td></tr> <tr><td>[List]</td></tr> </table>

