---
title: "Value.FromText | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.FromText

## Syntax

<pre>
Value.FromText(<b>text</b> as any, optional <b>culture</b> as nullable text) as any
</pre>  
  
## About  
Decodes a value from a textual representation, `text`, and interprets it as a value with an appropriate type. `Value.FromText` takes a text value and returns a number, a logical value, a null value, a datetime value, a duration value, or a text value. The empty text value is interpreted as a null value.
