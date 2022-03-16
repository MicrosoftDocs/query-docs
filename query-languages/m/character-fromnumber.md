---
description: "Learn more about: Character.FromNumber"
title: "Character.FromNumber | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Character.FromNumber

## Syntax

<pre>  
Character.FromNumber(<b>number</b> as nullable number) as nullable text
</pre>
  
## About

Returns the character equivalent of the number.

## Example 1

Given the number 9, find the character value.

**Usage**

```powerquery-m
Character.FromNumber(9)
```

**Output**

`"#(tab)"`
