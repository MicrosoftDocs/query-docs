---
title: "BinaryFormat.Transform | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BinaryFormat.Transform

  
## About  
Returns a binary format that will transform the values read by another binary format.  
  
## Syntax

<pre>   
BinaryFormat.Transform(binaryFormat as function, transform as function) as function  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binaryFormat|The binary format that will be used to read the value.|  
|transform|Invoked with the value read, and returns the transformed value.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m  
// Read a byte and add one to it.  
let      
binaryData = #binary({1}),      
transformFormat = BinaryFormat.Transform(          
BinaryFormat.Byte,          
(x) => x + 1)  
in  
transformFormat(binaryData)   
equals 2  
```  
