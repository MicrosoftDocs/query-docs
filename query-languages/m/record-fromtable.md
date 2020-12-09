---
title: "Record.FromTable | Microsoft Docs"
ms.date: 4/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Record.FromTable

## Syntax

<pre>
Record.FromTable(<b>table</b> as table) as record  
</pre>
  
## About  
Returns a record from a table of records `table` containing field names and value names `{[Name = name, Value = value]}`. An exception is thrown if the field names are not unique.

## Example 1
Create a record from the table of the form Table.FromRecords({[Name = "CustomerID", Value = 1], [Name = "Name", Value = "Bob"], [Name = "Phone", Value = "123-4567"]}).

```powerquery-m
Record.FromTable(
    Table.FromRecords({
        [Name = "CustomerID", Value = 1],
        [Name = "Name", Value = "Bob"],
        [Name = "Phone", Value = "123-4567"]
    })
)
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Name</th> <td>Bob</td> </tr> <tr> <th>Phone</th> <td>123-4567</td> </tr> </table>
