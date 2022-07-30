---
description: "Learn more about: Text.Clean"
title: "Text.Clean | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Text.Clean

## Syntax

<pre>
Text.Clean(<b>text</b> as nullable text) as nullable text
</pre>
  
## About

Returns a text value with all control characters of `text` removed.

## Example 1

Remove line feeds and other control characters from a text value.

**Usage**

```powerquery-m
Text.Clean("ABC#(lf)D")
```

**Output**

`"ABCD"`
