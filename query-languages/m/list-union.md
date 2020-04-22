---
title: "List.Union | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.Union

## Syntax

<pre>
List.Union(<b>lists</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>
  
## About  
Takes a list of lists `lists`, unions the items in the individual lists and returns them in the output list. As a result, the returned list contains all items in any input lists. This operation maintains traditional bag semantics, so duplicate values are matched as part of the Union. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing. 

## Example 1
Create a union of the list {1..5}, {2..6}, {3..7}.

```powerquery-m
List.Union({{1..5}, {2..6}, {3..7}})
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> <tr><td>6</td></tr> <tr><td>7</td></tr> </table>
