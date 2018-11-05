---
title: "Record.ToList | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.ToList

## Syntax

<pre>
Record.ToList(**record** as record) as list
</pre>

## About
Returns a list of values containing the field values from the input `record`.

## Example 
Extract the field values from a record.

```powerquery-m
Record.ToList([A = 1, B = 2, C = 3])
```


1

2

3

