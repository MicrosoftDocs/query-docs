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
`Uri.EscapeDataString(**data** as text) as text`
## About
Encodes special characters in the input `data` according to the rules of RFC 3986.

## Example 
Encode the special characters in "+money$".

`Uri.EscapeDataString("+money$")`

`"%2Bmoney%24"`

