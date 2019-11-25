---
title: "Text.SplitAny | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Text.SplitAny

## Syntax

<pre>
Text.SplitAny(<b>text</b> as text, <b>separators</b> as text) as list
</pre> 
  
## About  
Returns a list of text values resulting from the splitting a text value `text` based on any character in the specified delimiter, `separators`.

## Example 1
Create a list from the text value "Jamie|Campbell|Admin|Adventure Works|www.adventure-works.com".

```powerquery-m
Text.SplitAny("Jamie|Campbell|Admin|Adventure Works|www.adventure-works.com", "|")
```

<table> <tr><td>Jamie</td></tr> <tr><td>Campbell</td></tr> <tr><td>Admin</td></tr> <tr><td>Adventure Works</td></tr> <tr><td>www.adventure-works.com</td></tr> </table>
