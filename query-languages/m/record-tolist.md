---
title: "Record.ToList | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Record.ToList

## Syntax

<pre>
Record.ToList(<b>record</b> as record) as list
</pre>

## About
Returns a list of values containing the field values from the input `record`.

## Example 1
Extract the field values from a record.

```powerquery-m
Record.ToList([A = 1, B = 2, C = 3])
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> </table>
