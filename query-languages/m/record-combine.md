---
description: "Learn more about: Record.Combine"
title: "Record.Combine | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Record.Combine

## Syntax

<pre>
Record.Combine(<b>records</b> as list) as record
</pre>
  
## About  
Combines the records in the given `records`. If the `records` contains non-record values, an error is returned.

## Example 1
Create a combined record from the records.

```powerquery-m
Record.Combine({
    [CustomerID = 1, Name = "Bob"],
    [Phone = "123-4567"]
})
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Name</th> <td>Bob</td> </tr> <tr> <th>Phone</th> <td>123-4567</td> </tr> </table>
