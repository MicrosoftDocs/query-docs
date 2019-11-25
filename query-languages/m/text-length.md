---
title: "Text.Length | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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

```powerquery-m
Text.Length("Hello World")
```

`11`
