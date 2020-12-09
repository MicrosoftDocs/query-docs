---
title: "Logical.FromText | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Logical.FromText

## Syntax

<pre> 
Logical.FromText(<b>text</b> as nullable text) as nullable logical
</pre>
  
## About  
Creates a logical value from the text value `text`, either "true" or "false". If `text` contains a different string, an exception is thrown. The text value `text` is case insensitive.

## Example 1
Create a logical value from the text string "true".

```powerquery-m
Logical.FromText("true")
```

`true`

## Example 2
Create a logical value from the text string "a".

```powerquery-m
Logical.FromText("a")
```

`[Expression.Error] Could not convert to a logical.`
