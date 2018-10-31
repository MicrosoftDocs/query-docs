---
title: "Text.Select | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Select
`Text.Select(<b>text</b> as nullable text, <b>selectChars</b> as any) as nullable text`

## About
Returns a copy of the text value `text` with all the characters not in `selectChars` removed. 

####Example 1
Select all characters in the range of 'a' to 'z' from the text value.

`Text.Select("a,b;c", {"a".."z"})`

`"abc"`

