---
description: "Learn more about: Text.Repeat"
title: "Text.Repeat | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Text.Repeat("a", 5)
```

**Output**

`"aaaaa"`

## Example 2

Repeat the text "helloworld" three times.

**Usage**

```powerquery-m
Text.Repeat("helloworld.", 3)
```

**Output**

`"helloworld.helloworld.helloworld."`
