---
title: "List.Combine | Microsoft Docs"
ms.date: 7/26/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Combine

## Syntax

<pre> 
List.Combine(<b>lists</b> as list) as list 
</pre>

## About  
Takes a list of lists, <code>lists</code>, and merges them into a single new list. 

## Example 1

Combine the two simple lists {1, 2} and {3, 4}.

```powerquery-m
List.Combine({{1, 2}, {3, 4}})
```  

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> </table>

## Example 2

Combine the two lists, {1, 2} and {3, {4, 5}}, one of which contains a nested list.

```powerquery-m
List.Combine({{1, 2}, {3, {4, 5}}})
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>[List]</td></tr> </table>