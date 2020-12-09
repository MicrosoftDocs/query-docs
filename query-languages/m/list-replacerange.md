---
title: "List.ReplaceRange | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.ReplaceRange

## Syntax

<pre>
List.ReplaceRange(<b>list</b> as list, <b>index</b> as number, <b>count</b> as number, <b>replaceWith</b> as list) as list
</pre>
  
## About  
Replaces `count` values in the `list` with the list `replaceWith`, starting at specified position, `index`.

## Example 1
Replace {7, 8, 9} in the list {1, 2, 7, 8, 9, 5} with {3, 4}.

```powerquery-m
List.ReplaceRange({1, 2, 7, 8, 9, 5}, 2, 3, {3, 4})
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>
