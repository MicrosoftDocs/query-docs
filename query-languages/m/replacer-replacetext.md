---
title: "Replacer.ReplaceText | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Replacer.ReplaceText

## Syntax

<pre>
Replacer.ReplaceText(<b>text</b> as nullable text, <b>old</b> as text, <b>new</b> as text) as nullable text
</pre>
  
## About  
Replaces the `old` text in the original `text` with the `new` text. This replacer function can be used in `List.ReplaceValue` and `Table.ReplaceValue`.

## Example 1
Replace the text "hE" with "He" in the string "hEllo world".

```powerquery-m
Replacer.ReplaceText("hEllo world", "hE", "He")
```

`"Hello world"`
