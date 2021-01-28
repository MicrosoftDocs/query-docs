---
description: "Learn more about: Text.Clean"
title: "Text.Clean | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Clean

## Syntax

<pre>
Text.Clean(<b>text</b> as nullable text) as nullable text
</pre>
  
## About  
Returns a text value with all non-printable characters of `text` removed.

## Example 1
Remove line feeds and other non-printable characters from a text value.

```powerquery-m
Text.Clean("ABC#(lf)D")
```

`"ABCD"`
