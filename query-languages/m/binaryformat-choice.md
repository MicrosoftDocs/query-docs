---
title: "BinaryFormat.Choice | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BinaryFormat.Choice

  
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
