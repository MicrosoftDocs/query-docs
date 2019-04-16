---
title: "Record.FieldOrDefault | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FieldOrDefault

## About  

Returns the value of the specified field <code>field</code> in the record <code>record</code>. If the field is not found, the optional <code>defaultValue</code> is returned. 
  
## Syntax

<pre>
Record.FieldOrDefault(<b>record</b> as nullable record, <b>field</b> as text, optional <b>defaultValue</b> as any) as any
</pre>
  
## Example 1

Find the value of field "Phone" in the record, or return null if it doesn't exist.

```powerquery-m
Record.FieldOrDefault([CustomerID =1, Name="Bob"], "Phone")
```

`null`

## Example 2

Find the value of field "Phone" in the record, or return the default if it doesn't exist.

```powerquery-m
Record.FieldOrDefault([CustomerID =1, Name="Bob"], "Phone", "123-4567")
```

`"123-4567"`