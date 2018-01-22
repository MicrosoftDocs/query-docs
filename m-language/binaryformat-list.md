---
title: "BinaryFormat.List | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5e8812e9-699c-4e79-a82d-ea461dbfc6f6
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# BinaryFormat.List

  
## About  
Returns a binary format that reads a sequence of items and returns a list.  
  
```  
BinaryFormat.List(binaryFormat as function, optional countOrCondition as any) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binaryFormat|The binary format of each item.|  
|optional countOrCondition|See Remarks|  
  
## Remarks  
There are three ways to determine the number of items read:  
  
-   If the countOrCondition is not specified, then the binary format will read until there are no more items.  
  
-   If the countOrCondition is a number, then the binary format will read that many items.  
  
-   If the countOrCondition is a function, then that function will be invoked for each item read.  The function returns true to continue, and false to stop reading items.  The final item is included in the list.  
  
## Examples  
`// Read bytes until the end of the data.letbinaryData = #binary({1, 2, 3}),listFormat = BinaryFormat.List(BinaryFormat.Byte)inlistFormat(binaryData) equals {1, 2, 3}`  
  
```  
// Read two bytes.  
letbinaryData = #binary({1, 2, 3}),  
listFormat = BinaryFormat.List(BinaryFormat.Byte, 2)  
in  
listFormat(binaryData)   
equals {1, 2}  
```  
  
```  
// Read bytes until the byte value is greater than or equal to two.  
let  
binaryData = #binary({1, 2, 3}),  
listFormat = BinaryFormat.List(BinaryFormat.Byte, (x) => x < 2)  
in  
listFormat(binaryData)   
equals {1, 2}  
```  
