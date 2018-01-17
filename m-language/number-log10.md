---
title: "Number.Log10 | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6a73ab9e-fb67-4a57-9219-29b5b5a3f794
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.Log10
<code>Number.Log10(**number** as nullable number) as nullable number</code>

## About  
Returns the Base 10 logarithm of a number, <code>number</code>. If <code>number</code> is null <code>Number.Log10</code> returns null.
  
```  
Number.Log10 (number as nullable number)  as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|The number to calculate.|  
  
## Example 1
Get the base 10 logarithm of 2.


```
Number.Log10(2)
```


```
0.3010299956639812
```

