---
description: "Learn more about: RoundingMode.Type"
title: "RoundingMode.Type | Microsoft Docs"
ms.date: 5/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# RoundingMode.Type

## Definition

Specifies rounding direction when there is a tie between the possible numbers to round to.

## Allowed values
  
|Allowed value|Value|Description|
| ---------------- | --- | ----------- |
|**Up**|0|Round up when there is a tie between the possible numbers to round to.|
|**Down**|1|Round down when there is a tie between the possible numbers to round to.|
|**AwayFromZero**|2|Round away from zero when there is a tie between the possible numbers to round to.|
|**TowardZero**|3|Round toward zero when there is a tie between the possible numbers to round to.|
|**ToEven**|4|Round to the nearest even number when there is a tie between the possible numbers to round to.|

## Applies to

* [List functions](list-functions.md)
