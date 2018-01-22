---
title: "Percentage.From | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 94d9390a-daf7-4aac-b121-f485682bf2ea
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Percentage.From
<code>Percentage.From(**value** as any, optional **culture** as nullable text) as nullable number</code>

## About
Returns a <code>percentage</code> value from the given <code>value</code>. If the given <code>value</code> is <code>null</code>, <code>Percentage.From</code> returns <code>null</code>. If the given <code>value</code> is <code>text</code> with a trailing percent symbol, then the converted decimal number will be returned. Otherwise, see <code>Number.From</code> for converting it to <code>number</code> value.

## Example 1
Get the <code>percentage</code> value of <code>"12.3%"</code>.

<code>Percentage.From("12.3%")</code>

<code>0.123</code>



  
