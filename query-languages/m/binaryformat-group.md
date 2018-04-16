---
title: "BinaryFormat.Group | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BinaryFormat.Group

  
## About  
Returns a binary format that reads a group of items.  Each item value is preceded by a unique key value.  The result is a list of item values.  
  
```  
BinaryFormat.Group(binaryFormat as function, group as list, optional extra as nullable function, optional lastKey as any) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binaryFormat|The binary format of a key value.|  
|group|Provides information about a group of known items.|  
|Optional extra|Specifies a function that will return a binary format value for the value following any key that was unexpected. If the extra parameter is not specified, then an error will be raised if there are unexpected key values.|  
|Optional lastKey|Specifies the key that signals the end of the group.  If not specified, the group ends when the input ends.|  
  
### Occurrence values  
Occurrence values are used with **BinaryFormat.Group** to specify how many times an item in a group is expected to appear.  
  
-   Occurrence.Optional = 0  
  
-   Occurrence.Required = 1  
  
## Remarks  
The **group** parameter specifies a list of item definitions.  Each item definition is a list, containing 3-5 values, as follows:  
  
-   **Key value**.  A value of a key that corresponds to an item. This must be unique within a set of items.  
  
-   **Item format**.  A binary format corresponding to a value of an item. This allows each item to have a different format.  
  
-   **Item occurrence**.  The occurrence value for how many times an item is expected to appear in a group. Required items that are not present cause an error.  Required or optional duplicate items are handled like unexpected key values.  
  
-   **Default item value (optional)**.  If a default item value appears in an item definition list and is not null, then it will be used instead of the default. The default for repeating or optional items is null, and the default for repeating values is an empty list { }.  
  
-   **Item value transform (optional)**.   If an item value transform function is present in an item definition list and is not null, then it will be called to transform an item value before it is returned. The transform function is only called if the item appears in the input (it will never be called with the default value).  
  
## Examples  
The following assumes a key value that is a single byte, with 4 expected items in the group, all of which have a byte of data following the key.  The items appear in the input as follows:  
  
-   Key 1 is required, and does appear with value 11.  
  
-   Key 2 repeats, and appears twice with value 22, and results in a value of { 22, 22 }.  
  
-   Key 3 is optional, and does not appear, and results in a value of null.  
  
-   Key 4 repeats, but does not appear, and results in a value of { }.  
  
-   Key 5 is not part of the group, but appears once with value 55.  The extra function is called with the key value 5, and returns the format corresponding to that value (BinaryFormat.Byte).  The value 55 is read and discarded.  
  
    ```  
    let      
    b = #binary(      
    {           
    1, 11,           
    2, 22,           
    2, 22,           
    5, 55,           
    1, 11       
    }),      
    f = BinaryFormat.Group(          
    BinaryFormat.Byte,          
    {              
    { 1, BinaryFormat.Byte, Occurrence.Required },              
    { 2, BinaryFormat.Byte, Occurrence.Repeating },                    
    { 3, BinaryFormat.Byte, Occurrence.Optional },              
    { 4, BinaryFormat.Byte, Occurrence.Repeating }          
    },          
    (extra) => BinaryFormat.Byte)  
    in      
    f(b)  
    // { 11, { 22, 22 }, null, { } }  
    ```  
  
The following example illustrates the item value transform and default item value.   The repeating item with key 1 sums the list of values read using List.Sum.  The optional item with key 2 has a default value of 123 instead of null.  
  
```  
let      
b = #binary(      
{           
1, 101,           
1, 102       
}),      
f = BinaryFormat.Group(          
BinaryFormat.Byte,          
{              
{ 1, BinaryFormat.Byte, Occurrence.Repeating,                 
0, (list) => List.Sum(list) },              
{ 2, BinaryFormat.Byte, Occurrence.Optional, 123 }          
})  
in      
f(b)  
// { 203, 123 }  
```  
