---
title: "List.RemoveItems | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.RemoveItems

## Syntax

<pre>
List.RemoveItems(<b>list1</b> as list, <b>list2</b> as list) as list
</pre>
  
## About  
Removes all occurrences of the given values in the `list2` from `list1`. If the values in `list2` don't exist in `list1`, the original list is returned.

## Example 1
Remove the items in the list {2, 4, 6} from the list {1, 2, 3, 4, 2, 5, 5}.

```powerquery-m
List.RemoveItems({1, 2, 3, 4, 2, 5, 5}, {2, 4, 6})
```

<table> <tr><td>1</td></tr> <tr><td>3</td></tr> <tr><td>5</td></tr> <tr><td>5</td></tr> </table>
