---
description: "Learn more about: PercentileMode.Type"
title: "PercentileMode.Type | Microsoft Docs"
ms.date: 5/3/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# PercentileMode.Type

## Definition

Specifies the percentile mode type.
  
## Fields

|Enumeration|Value|Description|  
|------------|-----|---------------|  
|**ExcelExc**|2| When interpolating values for [List.Percentile](list-percentile.md), use a method compatible with Excel's `PERCENTILE.EXC`.|
|**ExcelInc**|1| When interpolating values for **List.Percentile**, use a method compatible with Excel's `PERCENTILE.INC`.|
|**SqlCont**|4| When interpolating values for **List.Percentile**, use a method compatible with SQL Server's `PERCENTILE_CONT`.|
|**SqlDisc**|3| When interpolating values for **List.Percentile**, use a method compatible with SQL Server's `PERCENTILE_DISC`.|
  