---
title: "List.IsEmpty | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.IsEmpty

## Syntax

<pre>
List.IsEmpty(<b>list</b> as list) as logical
</pre>
  
## About  
Returns `true` if the list, `list`, contains no values (length 0). If the list contains values (length > 0), returns `false`.

## Example 1
Find if the list {} is empty.

```powerquery-m
List.IsEmpty({})
```

`true`

## Example 2
Find if the list {1, 2} is empty.

```powerquery-m
List.IsEmpty({1, 2})
```

`false`
