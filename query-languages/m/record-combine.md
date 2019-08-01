---
title: "Record.Combine | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
Record.Combine({ [CustomerID =1, Name ="Bob"] , [Phone = "123-4567"]})
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Name</th> <td>Bob</td> </tr> <tr> <th>Phone</th> <td>123-4567</td> </tr> </table>
