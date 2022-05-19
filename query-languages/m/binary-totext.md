---
description: "Learn more about: Binary.ToText"
title: "Binary.ToText | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Binary.ToText

## Syntax

<pre>
Binary.ToText(<b>binary</b> as nullable binary, optional <b>encoding</b> as nullable number) as nullable text 
</pre> 
  
## About  
Returns the result of converting a binary list of numbers `binary` into a text value. Optionally, `encoding` may be specified to indicate the encoding to be used in the text value produced The following `BinaryEncoding` values may be used for `encoding`. <ul> <li><code>BinaryEncoding.Base64</code>: Base 64 encoding</li> <li><code>BinaryEncoding.Hex</code>: Hex encoding</li> </ul>
  
