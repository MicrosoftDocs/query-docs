---
title: "Text.InferNumberType | Microsoft Docs"
ms.date: 6/13/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.InferNumberType

## Syntax

<pre>
Text.InferNumberType(<b>text</b> as text, optional <b>culture</b> as nullable text) as type 
</pre>
  
## About  
Inters granular number type (Int64.Type, Double.Type, etc.) of <code>text</code> using <code>culture</code>. Exception is raised if <code>text</code> is not a number  
  