---
title: "Text.InferNumberType | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.InferNumberType

## Syntax

<pre>
Text.InferNumberType(<b>text</b> as text, optional <b>culture</b> as nullable text) as type
</pre>
  
## About  
Infers the granular number type (Int64.Type, Double.Type, etc.) of `text`. An error is raised if `text` is not a number. An optional `culture` may also be provided (for example, "en-US").
  