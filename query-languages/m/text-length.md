---
description: "Learn more about: Text.Length"
title: "Text.Length | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Text.Length

## Syntax

<pre>
Text.Length(<b>text</b> as nullable text) as nullable number
</pre>
  
## About

Returns the number of characters in the text `text`.

## Example 1

Find how many characters are in the text "Hello World".

**Usage**

```powerquery-m
Text.Length("Hello World")
```

**Output**

`11`
