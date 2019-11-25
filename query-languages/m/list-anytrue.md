---
title: "List.AnyTrue | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.AnyTrue

## Syntax

<pre>
List.AnyTrue(<b>list</b> as list) as logical
</pre>
  
## About  
Returns true if any expression in the list `list` is true.

## Example 1
Determine if any of the expressions in the list {true, false, 2 > 0} are true.

```powerquery-m
List.AnyTrue({true, false, 2>0})
```

`true`

## Example 2
Determine if any of the expressions in the list {2 = 0, false, 2 < 0} are true.

```powerquery-m
List.AnyTrue({2 = 0, false, 2 < 0})
```

`false`
