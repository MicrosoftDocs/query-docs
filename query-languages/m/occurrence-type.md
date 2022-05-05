---
description: "Learn more about: Occurrence.Type"
title: "Occurrence.Type | Microsoft Docs"
ms.date: 5/5/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Occurrence.Type

## Definition

Specifies the occurrence of an element in a sequence.

## Fields

|Field|Value|Description|
| ------- | --- | ----------- |
|**All**|2|A list of positions of all occurrences of the found values is returned.|
|**First**|0|The position of the first occurrence of the found value is returned.|
|**Last**|1|The position of the last occurrence of the found value is returned.|
|**Optional**|0|The item is expected to appear zero or one time in the input.|
|**Repeating**|2|The item is expected to appear zero or more times in the input.|
|**Required**|1|The item is expected to appear once in the input.|
