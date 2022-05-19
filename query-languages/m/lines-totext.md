---
description: "Learn more about: Lines.ToText"
title: "Lines.ToText | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Lines.ToText

## Syntax

<pre>
Lines.ToText(<b>lines</b> as list, optional <b>lineSeparator</b> as nullable text) as text 
</pre>
  
## About  
Converts a list of text into a single text. The specified lineSeparator is appended to each line. If not specified then the carriage return and line feed characters are used.
