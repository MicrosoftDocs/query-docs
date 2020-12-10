---
title: "Text.ToList | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.ToList

## Syntax

<pre>
Text.ToList(<b>text</b> as text) as list 
</pre>
  
## About  
Returns a list of character values from the given text value `text`.

## Example 1
Create a list of character values from the text "Hello World".

```powerquery-m
Text.ToList("Hello World")
```

<table> <tr><td>H</td></tr> <tr><td>e</td></tr> <tr><td>l</td></tr> <tr><td>l</td></tr> <tr><td>o</td></tr> <tr><td> </td></tr> <tr><td>W</td></tr> <tr><td>o</td></tr> <tr><td>r</td></tr> <tr><td>l</td></tr> <tr><td>d</td></tr> </table>
