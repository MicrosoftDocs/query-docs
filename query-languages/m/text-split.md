---
description: "Learn more about: Text.Split"
title: "Text.Split | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Split

## Syntax

<pre>
Text.Split(<b>text</b> as text, <b>separator</b> as text) as list
</pre> 
  
## About  
Returns a list of text values resulting from the splitting a text value `text` based on the specified delimiter, `separator`.

## Example 1
Create a list from the "|" delimited text value "Name|Address|PhoneNumber".

```powerquery-m
Text.Split("Name|Address|PhoneNumber", "|")
```

<table> <tr><td>Name</td></tr> <tr><td>Address</td></tr> <tr><td>PhoneNumber</td></tr> </table>
