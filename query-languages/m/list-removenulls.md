---
title: "List.RemoveNulls | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.RemoveNulls

## Syntax

<pre>
List.RemoveNulls(<b>list</b> as list) as list 
</pre>
  
## About  
Removes all occurrences of "null" values in the `list`. If there are no 'null' values in the list, the original list is returned.

## Example 1
Remove the "null" values from the list {1, 2, 3, null, 4, 5, null, 6}.

```powerquery-m
List.RemoveNulls({1, 2, 3, null, 4, 5, null, 6})
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> <tr><td>6</td></tr> </table>
