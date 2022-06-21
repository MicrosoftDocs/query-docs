---
description: "Learn more about: Text.Start"
title: "Text.Start | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Text.Start

## Syntax

<pre>
Text.Start(<b>text</b> as nullable text, <b>count</b> as number) as nullable text
</pre>
  
## About

Returns the first `count` characters of `text` as a text value.

## Example 1

Get the first 5 characters of "Hello, World".

**Usage**

```powerquery-m
Text.Start("Hello, World", 5)
```

**Output**

`"Hello"`
