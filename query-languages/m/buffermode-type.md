---
description: "Learn more about: BufferMode.Type"
title: "BufferMode.Type | Microsoft Docs"
ms.date: 5/16/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# BufferMode.Type

## Definition

Describes the type of buffering to be performed.

## Allowed values

|Name|Value|Description|  
|------------|--|---------------|  
|**BufferMode.Eager**|1|The entire value is immediately buffered in memory before continuing.|
|**BufferMode.Delayed**|2|The type of the value is computed immediately but its contents aren't buffered until data is needed, at which point the entire value is immediately buffered.|

## Applies to

* [Accessing data functions](accessing-data-functions.md)
