---
title: "Binary.End | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 19de11e9-2c4d-4cf0-ac1d-6e4ceeab384d
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Binary.End
<code>Binary.End(<b>binary</b> as binary) as binary</code>  
## About  
<p>Returns a binary value corresponding to the end of <code>binary</code>. The returned value is always empty (i.e. it is 0 bytes in length).</p> <p><code>Binary.End</code> can be used to append to a binary value by replacing the end of the binary value.</p>  
  
## Example 1  
Return the end of a binary value.  
  
<code>Binary.End(Text.ToBinary("Hello world!"))</code>  
  
<code>Binary.FromText("", BinaryEncoding.Base64)</code>  
