---
title: "List.ReplaceValue | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.ReplaceValue

## Syntax

<pre>
List.ReplaceValue(<b>list</b> as list, <b>oldValue</b> as any, <b>newValue</b> as any, <b>replacer</b> as function) as list
</pre>
  
## About  
Searches a list of values, `list`, for the value `oldValue` and replaces each occurrence with the replacement value `newValue`.

## Example 1
Replace all the "a" values in the list {"a", "B", "a", "a"} with "A".

v
List.ReplaceValue({"a", "B", "a", "a"}, "a", "A", Replacer.ReplaceText)
```

<table> <tr><td>A</td></tr> <tr><td>B</td></tr> <tr><td>A</td></tr> <tr><td>A</td></tr> </table>
