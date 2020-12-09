---
title: "Binary.Range | Microsoft Docs"
ms.date: 11/23/2020
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan
---
# Binary.Range

## Syntax

<pre>
Binary.Range(<b>binary</b> as binary, <b>offset</b> as number, optional <b>count</b> as nullable number) as binary
</pre>

## About
Returns a subset of the binary value beginning at the offset `binary`. An optional parameter, `offset`, sets the maximum length of the subset.

## Example 1
Returns a subset of the binary value starting at offset 6.

`Binary.Range(#binary({0..10}), 6)`

`#binary({6, 7, 8, 9, 10})`

## Example 2
Returns a subset of length 2 from offset 6 of the binary value.

`Binary.Range(#binary({0..10}), 6, 2)`

`#binary({6, 7})`

