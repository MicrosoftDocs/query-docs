---
title: "List.Last | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Last

## Syntax

<pre>
List.Last(<b>list</b> as list, optional <b>defaultValue</b> as any) as any 
</pre>
  
## About  
Returns the last item in the list `list`, or the optional default value, `defaultValue`, if the list is empty. If the list is empty and a default value is not specified, the function returns `null`.

## Example 1
Find the last value in the list {1, 2, 3}.

```powerquery-m
List.Last({1, 2, 3})
```

`3`

## Example 2
Find the last value in the list {} or -1 if it empty.

```powerquery-m
List.Last({}, -1)
```

`-1`
