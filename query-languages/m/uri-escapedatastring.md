---
title: "Uri.EscapeDataString | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4c9d75d6-7419-490a-af60-9c07afff171f
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Uri.EscapeDataString
<code>Uri.EscapeDataString(**data** as text) as text</code>
## About
Encodes special characters in the input <code>data</code> according to the rules of RFC 3986.

## Example 
Encode the special characters in "+money$".

<code>Uri.EscapeDataString("+money$")</code>

<code>"%2Bmoney%24"</code>

