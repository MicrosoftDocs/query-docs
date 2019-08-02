---
title: "Text.Remove | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Remove

## Syntax

<pre>
Text.Remove(<b>text</b> as nullable text, <b>removeChars</b> as any) as nullable text
</pre>
  
## About  
Returns a copy of the text value `text` with all the characters from `removeChars` removed. 

## Example 1
Remove characters , and ; from the text value.

```powerquery-m
Text.Remove("a,b;c",{",",";"})
```

`"abc"`
