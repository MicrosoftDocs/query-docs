---
description: "Learn more about: Record.FromList"
title: "Record.FromList | Microsoft Docs"
ms.date: 3/9/2022
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

**Usage**

```powerquery-m
Record.FromList({1, "Bob", "123-4567"}, {"CustomerID", "Name", "Phone"})
```

**Output**

`[CustomerID = 1, Name = "Bob", Phone = "123-4567"]`

## Example 2

Build a record from a list of field values and a record type.

**Usage**

```powerquery-m
Record.FromList({1, "Bob", "123-4567"}, type [CustomerID = number, Name = text, Phone = number])
```

**Output**

`[CustomerID = 1, Name = "Bob", Phone = "123-4567"]`
