---
description: "Learn more about: MissingField.Type"
title: "MissingField.Type | Microsoft Docs"
ms.date: 5/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# MissingField.Type

## Definition

Specifies the expected action for missing values in a row that contains columns less than expected.

## Allowed values

|Allowed fields|Value|Description|
|-----|-----|-----------|
|**Error**| 0 |Indicates that missing fields should result in an error. (This is the default value.)|
|**Ignore**| 1 |Indicates that missing fields should be ignored.|
|**UseNull**| 2 |Indicates that missing fields should be included as null values.|

## Applies to

* [Record functions](record-functions.md)
* [Table functions](table-functions.md)
