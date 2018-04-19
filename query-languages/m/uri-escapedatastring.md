---
title: "Uri.EscapeDataString | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Uri.EscapeDataString
<code>Uri.EscapeDataString(**data** as text) as text</code>
## About
Encodes special characters in the input <code>data</code> according to the rules of RFC 3986.

## Example 
Encode the special characters in "+money$".

<code>Uri.EscapeDataString("+money$")</code>

<code>"%2Bmoney%24"</code>

