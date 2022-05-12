---
description: "Learn more about: PercentileMode.Type"
title: "PercentileMode.Type | Microsoft Docs"
ms.date: 5/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# PercentileMode.Type

## Definition

Specifies the percentile mode type.
  
## Allowed values

|Allowed value|Value|Description|  
|------------|-----|---------------|  
|**ExcelInc**|1| When interpolating values for [List.Percentile](list-percentile.md), use a method compatible with Excel's [PERCENTILE.INC](https://support.microsoft.com/office/percentile-inc-function-680f9539-45eb-410b-9a5e-c1355e5fe2ed?msclkid=edba39d1d15911ecaec6b493dc604bae).|
|**ExcelExc**|2| When interpolating values for **List.Percentile**, use a method compatible with Excel's [PERCENTILE.EXC](https://support.microsoft.com/office/percentile-exc-function-bbaa7204-e9e1-4010-85bf-c31dc5dce4ba).|
|**SqlDisc**|3| When interpolating values for **List.Percentile**, use a method compatible with SQL Server's [PERCENTILE_DISC](/sql/t-sql/functions/percentile-disc-transact-sql).|
|**SqlCont**|4| When interpolating values for **List.Percentile**, use a method compatible with SQL Server's [PERCENTILE_CONT](/sql/t-sql/functions/percentile-cont-transact-sql).|

## Applies to

* [List functions](list-functions.md)
