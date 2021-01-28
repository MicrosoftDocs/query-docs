---
description: "Learn more about: List.Range"
title: "List.Range | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Range

## Syntax

<pre>
List.Range(<b>list</b> as list, <b>offset</b> as number, optional <b>count</b> as nullable number) as list 
</pre>
  
## About  
Returns a subset of the list beginning at the offset `list`. An optional parameter, `offset`, sets the maximum number of items in the subset.

## Example 1
Find the subset starting at offset 6 of the list of numbers 1 through 10.

```powerquery-m
List.Range({1..10}, 6)
```

<table> <tr><td>7</td></tr> <tr><td>8</td></tr> <tr><td>9</td></tr> <tr><td>10</td></tr> </table>

## Example 2
Find the subset of length 2 from offset 6, from the list of numbers 1 through 10.

```powerquery-m
List.Range({1..10}, 6, 2)
```

<table> <tr><td>7</td></tr> <tr><td>8</td></tr> </table>
