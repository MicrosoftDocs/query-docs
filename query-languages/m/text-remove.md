---
title: "Text.Remove | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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
Text.Remove("a,b;c", {",",";"})
```

`"abc"`
