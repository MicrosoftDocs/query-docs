---
title: "CUSTOMDATA Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql.as.daxref.CUSTOMDATA.f1"
ms.assetid: 58235ad8-226c-43cc-8a69-5a52ac19dd4e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# CUSTOMDATA Function (DAX)
Returns the content of the **CustomData** property in the connection string.  
  
## Syntax  
  
```  
CUSTOMDATA()  
```  
  
## Return Value  
The content of the **CustomData** property in the connection string.  
  
Blank, if **CustomData** property was not defined at connection time.  
  
## Exceptions  
  
## Remarks  
  
## Example  
The following DAX code verifies if the CustomData property was set to **"OK"**.  
  
```  
=IF(CUSTOMDATA()="OK", "Correct Custom data in connection string", "No custom data in connection string property or unexpected value")  
```  
