---
title: "#binary | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: eea0c962-a7de-4b99-987f-e9d8e955e245
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# #binary
<code>#binary(<b>value</b> as any) as any</code>
## About
Creates a binary value from a list of numbers or a base 64 encoded text value.

## Example 1
Create a binary value from a list of numbers.

<code>#binary({0x30, 0x31, 0x32})</code>

<code>Text.ToBinary("012")</code>

## Example 2
Create a binary value from a base 64 encoded text value.

<code>#binary("1011")</code>

<code>Binary.FromText("1011", BinaryEncoding.Base64)</code>
  
