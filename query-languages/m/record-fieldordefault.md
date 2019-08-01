---
title: "Record.FieldOrDefault | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FieldOrDefault

## Syntax

<pre>
Record.FieldOrDefault(<b>record</b> as nullable record, <b>field</b> as text, optional <b>defaultValue</b> as any) as any
</pre>

## About  
Returns the value of the specified field `field` in the record `record`. If the field is not found, the optional `defaultValue` is returned.

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
