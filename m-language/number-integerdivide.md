---
title: "Number.IntegerDivide | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1af4109a-2b61-4b7d-bf68-0e2f654149f9
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.IntegerDivide

  
## About  
Divides two numbers and returns the whole part of the resulting number.  
  
```  
Number.IntegerDivide (number1 as nullable number,  number2 as nullable number,  optional precision as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number1|The Dividend.|  
|number2|The Divisor.|  
|optional precision|Precision of the result.|  
  
## Example  
  
```  
Number.IntegerDivide(9.2, 3.1) equals 2  
```  
