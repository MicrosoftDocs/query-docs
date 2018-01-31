---
title: "Text.Select | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f8ff1db3-2ca0-4b4c-9eb7-e8ba893c4abf
caps.latest.revision: 3
author: "MarkMcGeeAtAquent"
ms.author: "v-mamcge"
manager: "kfile"
---
# Text.Select
<code>Text.Select(<b>text</b> as nullable text, <b>selectChars</b> as any) as nullable text</code>

## About
Returns a copy of the text value `text` with all the characters not in `selectChars` removed. 

####Example 1
Select all characters in the range of 'a' to 'z' from the text value.

`Text.Select("a,b;c", {"a".."z"})`

`"abc"`

