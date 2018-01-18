---
title: "Lines.FromBinary | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f7b4d881-e51a-4dd4-8307-8dce8e5654fb
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Lines.FromBinary
<code>Lines.FromBinary(**binary** as binary, optional **quoteStyle** as nullable number, optional **includeLineSeparators** as nullable logical, optional **encoding** as nullable number) as list</code>

## About
Converts a binary value to a list of text values split at lines breaks. If a quote style is specified, then line breaks may appear within quotes. If includeLineSeparators is true, then the line break characters are included in the text.