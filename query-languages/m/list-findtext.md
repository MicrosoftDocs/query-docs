---
title: "List.FindText | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.FindText

## Syntax

<pre>
List.FindText(<b>list</b> as list, <b>text</b> as text) as list
</pre>
  
## About  
Returns a list of the values from the list `list` which contained the value `text`.

## Example 1
Find the text values in the list {"a", "b", "ab"} that match "a". 

```powerquery-m
List.FindText({"a", "b", "ab"}, "a")
```

<table> <tr><td>a</td></tr> <tr><td>ab</td></tr> </table>
