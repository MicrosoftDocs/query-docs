---
title: "Record.AddField | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Record.AddField

## Syntax

<pre>
Record.AddField(<b>record</b> as record, <b>fieldName</b> as text, <b>value</b> as any, optional <b>delayed</b> as nullable logical) as record 
</pre>
  
## About  
Adds a field to a record `record`, given the name of the field `fieldName` and the value `value`.

## Example 1
Add the field Address to the record.

```powerquery-m
Record.AddField([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "Address", "123 Main St.")
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Name</th> <td>Bob</td> </tr> <tr> <th>Phone</th> <td>123-4567</td> </tr> <tr> <th>Address</th> <td>123 Main St.</td> </tr> </table>
