---
description: "Learn more about: Text.SplitAny"
title: "Text.SplitAny | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Text.SplitAny("Jamie|Campbell|Admin|Adventure Works|www.adventure-works.com", "|")
```

**Output**

```powerquery-m
{
    "Jamie",
    "Campbell",
    "Admin",
    "Adventure Works",
    "www.adventure-works.com"
}
```
