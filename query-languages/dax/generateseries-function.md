---
title: "GENERATESERIES Function | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7c541ef4-c6a4-4163-b972-01e5f652ec04
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# GENERATESERIES Function
Returns a single column table containing the values of an arithmetic series, that is, a sequence of values in which each differs from the preceding by a constant quantity. The name of the column returned is Value.  
  
## Syntax  
  
```  
GENERATESERIES(<startValue>, <endValue>[, <incrementValue>])
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|startValue|The initial value used to generate the sequence.|
|endValue|The end value used to generate the sequence.|  
|incrementValue|(Optional) The increment value of the sequence. When not provided, the default value is 1.|    
  
## Return Value  
A single column table containing the values of an arithmetic series. The name of the column is Value.
  
## Remarks  
When startValue is less than endValue, an empty table is returned.

incrementValue must be a positive value.

The sequence stops at the last value that is less than or equal to endValue.

  
## Examples
### Example 1
The following DAX query:
```
EVALUATE GENERATESERIES(1, 5)
```
Returns the following table with a single column:

[Value]  | | 
---------|---------
1     |         
2     |         
3     |         
4     |         
5     |         

### Example 2
The following DAX query:
```
EVALUATE GENERATESERIES(1.2, 2.4, 0.4)
```
Returns the following table with a single column:

[Value]  | | 
---------|---------
1.2    |         
1.6     |         
2     |         
2.4     |           

### Example 3
The following DAX query:
```
EVALUATE GENERATESERIES(CURRENCY(10), CURRENCY(12.4), CURRENCY(0.5))
```
Returns the following table with a single column:

[Value]  | | 
---------|---------
10    |         
10.5     |         
11     |         
11.5     |     
12     |