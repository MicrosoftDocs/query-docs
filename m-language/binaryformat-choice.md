---
title: "BinaryFormat.Choice | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 08ef8f38-b8c3-40ab-b6ed-f48b61a91117
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# BinaryFormat.Choice
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a binary format that chooses the next binary format based on a value that has already been read.  
  
```  
BinaryFormat.Choice(binaryFormat as function, choice as function, optional type as nullable type) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binaryFormat|The binary format that will be used to read the value.|  
|choice|Choice for the next binary format.|  
|optional type|Tthe type of binary format that will be returned by the choice function.  Either type any, type list, or type binary may be specified.|  
  
## Remarks  
  
-   If type list or type binary is used, then the system may be able to return a streaming binary or list value instead of a buffered one, which may reduce the amount of memory necessary to read the format.  
  
-   The binary format value produced by this function is processed in five stages:  
  
-   The specified binaryFormat is used to read a value.  
  
-   The value is passed to the choice function.  
  
-   The choice function inspects the value and returns a second binary format.  
  
-   The second binary format is used to read a second value.  
  
-   The second value is returned.  
  
-   To preserve the first value read, a record binary format can be used to echo the value as a field.  
  
## Examples  
// Read a list of bytes where number of elements is determined by the first byte.  
  
```  
let      
binaryData = #binary({2, 3, 4, 5}),      
listFormat = BinaryFormat.Choice(          
BinaryFormat.Byte,          
(length) => BinaryFormat.List(BinaryFormat.Byte, length))  
in      
listFormat(binaryData)   
equals {3, 4}  
```  
// Read a list of bytes where the number of elements is determined by the first byte, and preserve the first byte read.  
  
```  
let      
binaryData = #binary({2, 3, 4, 5}),   
listFormat = BinaryFormat.Choice(          
BinaryFormat.Byte,         
(length) => BinaryFormat.Record([              
length = length,              
list = BinaryFormat.List(BinaryFormat.Byte, length)          
]))  
in      
listFormat(binaryData)   
equals [ length = 2, list = {3, 4} ]  
```  
// Read a list of bytes where number of elements is determined by the first byte using a streaming list.  
  
```  
let      
binaryData = #binary({2, 3, 4, 5}),      
listFormat = BinaryFormat.Choice(          
BinaryFormat.Byte,          
(length) => BinaryFormat.List(BinaryFormat.Byte, length),          
type list)  
in      
listFormat(binaryData)   
equals {3, 4}  
```  
