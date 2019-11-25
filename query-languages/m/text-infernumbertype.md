---
title: "Text.InferNumberType | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Text.InferNumberType

## Syntax

<pre>
Text.InferNumberType(<b>text</b> as text, optional <b>culture</b> as nullable text) as type
</pre>
  
## About  
Infers granular number type (Int64.Type, Double.Type, etc.) of `text` using `culture`. Exception is raised if `text` is not a number
  