---
description: "Learn more about: CUSTOMDATA"
title: "CUSTOMDATA function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# CUSTOMDATA

Returns the content of the **CustomData** property in the connection string.  
  
## Syntax  
  
```dax
CUSTOMDATA()  
```
  
## Return value

The content of the **CustomData** property in the connection string.  
  
Blank, if **CustomData** property was not defined at connection time.  

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX formula verifies if the CustomData property was set to **"OK"**.  
  
```dax
= IF(CUSTOMDATA()="OK", "Correct Custom data in connection string", "No custom data in connection string property or unexpected value")  
```
