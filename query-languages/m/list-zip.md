---
title: "List.Zip | Microsoft Docs"
ms.date: 7/26/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

<table> <tr><td>[List]</td></tr> <tr><td>[List]</td></tr> </table>


## Example 2
Zips the two simple lists of different lengths {1, 2} and {3}.

```powerquery-m
List.Zip({{1, 2}, {3}})
```

<table> <tr><td>[List]</td></tr> <tr><td>[List]</td></tr> </table>

