---
title: "Record.FromList | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Record.FromList

## Syntax

<pre>
Record.FromList(<b>list</b> as list, <b>fields</b> as any) as record
</pre>
  
## About  
Returns a record given a `list` of field values and a set of fields. The `fields` can be specified either by a list of text values, or a record type. An error is thrown if the fields are not unique.

## Example 1
Build a record from a list of field values and a list of field names.

```powerquery-m
Record.FromList({1, "Bob", "123-4567"}, {"CustomerID", "Name", "Phone"})
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Name</th> <td>Bob</td> </tr> <tr> <th>Phone</th> <td>123-4567</td> </tr> </table>

## Example 2
Build a record from a list of field values and a record type.

```powerquery-m
Record.FromList({1, "Bob", "123-4567"}, type [CustomerID = number, Name = text, Phone = number])
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Name</th> <td>Bob</td> </tr> <tr> <th>Phone</th> <td>123-4567</td> </tr> </table>
