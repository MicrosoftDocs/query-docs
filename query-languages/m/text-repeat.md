---
title: "Text.Repeat | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Repeat

## Syntax

<pre>
Text.Repeat(<b>text</b> as nullable text, <b>count</b> as number) as nullable text 
</pre>
  
## About  
Returns a text value composed of the input text `text` repeated `count` times.

## Example 1
Repeat the text "a" five times.

```powerquery-m
Text.Repeat("a", 5)
```

`"aaaaa"`

## Example 2
Repeat the text "helloworld" three times.

```powerquery-m
Text.Repeat("helloworld.", 3)
```

`"helloworld.helloworld.helloworld."`
