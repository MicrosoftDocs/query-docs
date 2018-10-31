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
`#binary(<b>value</b> as any) as any`
## About
Creates a binary value from a list of numbers or a base 64 encoded text value.

## Example 1
Create a binary value from a list of numbers.

`#binary({0x30, 0x31, 0x32})`

`Text.ToBinary("012")`

## Example 2
Create a binary value from a base 64 encoded text value.

`#binary("1011")`

`Binary.FromText("1011", BinaryEncoding.Base64)`
  
