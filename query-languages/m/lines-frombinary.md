---
title: "Lines.FromBinary | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Lines.FromBinary
<code>Lines.FromBinary(**binary** as binary, optional **quoteStyle** as nullable number, optional **includeLineSeparators** as nullable logical, optional **encoding** as nullable number) as list</code>

## About
Converts a binary value to a list of text values split at lines breaks. If a quote style is specified, then line breaks may appear within quotes. If includeLineSeparators is true, then the line break characters are included in the text.