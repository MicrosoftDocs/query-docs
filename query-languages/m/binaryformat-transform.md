---
title: "BinaryFormat.Transform | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6c3567f6-5d85-48bf-9533-c22675dff3a4
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# BinaryFormat.Transform

  
## About  
Returns a binary format that will transform the values read by another binary format.  
  
```  
BinaryFormat.Transform(binaryFormat as function, transform as function) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binaryFormat|The binary format that will be used to read the value.|  
|transform|Invoked with the value read, and returns the transformed value.|  
  
## <a name="__goback"></a>Example  
  
```  
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
