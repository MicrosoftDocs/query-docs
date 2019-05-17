---
title: "List.Zip | Microsoft Docs"
ms.date: 5/17/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Zip

## Syntax

<pre>
List.Zip(<b>lists</b> as list) as list
</pre>

## About
Takes a list of lists, `lists`, and returns a list of lists combining items at the same position.

## Example 1
Zips the two simple lists {1, 2} and {3, 4}.

```powerquery-m
List.Zip({{1, 2}, {3, 4}})
```

<code>{ { 1, 3 }, { 2, 4 } }</code>

## Example 2
Zips the two simple lists of different lengths {1, 2} and {3}.

```powerquery-m
List.Zip({{1, 2}, {3}})
```

<code>{ { 1, 3 }, { 2, null } }</code> 
