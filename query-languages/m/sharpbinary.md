---
title: "#binary | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
  
