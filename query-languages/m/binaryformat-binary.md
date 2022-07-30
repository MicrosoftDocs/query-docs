---
description: "Learn more about: BinaryFormat.Binary"
title: "BinaryFormat.Binary"
ms.date: 7/29/2019
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# BinaryFormat.Binary

## Syntax

<pre>
BinaryFormat.Binary(optional <b>length</b> as any) as function</code>
</pre>
  
## About  
Returns a binary format that reads a binary value. If `length` is specified, the binary value will contain that many bytes. If `length` is not specified, the binary value will contain the remaining bytes. The `length` can be specified either as a number, or as a binary format of the length that preceeds the binary data.  
  
