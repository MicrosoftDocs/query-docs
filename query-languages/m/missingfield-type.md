---
description: "Learn more about: MissingField.Type"
title: "MissingField.Type | Microsoft Docs"
ms.date: 5/3/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# MissingField.Type

## Definition

Specifies the expected action for missing values in a row that contains columns less than expected.

## Fields

|Field|Value|Description|
|-----|-----|-----------|
|**Error**| 0 |Indicates that missing fields should result in an error. (This is the default value.)|
|**Ignore**| 1 |Indicates that missing fields should be ignored.|
|**UseNull**| 2 |Indicates that missing fields should be included as null values.|

## Remarks

These fields are used in optional parameters in both record and table functions. The functions that use the optional `missingField` parameter are:

* [Record.RemoveFields](record-removefields.md)
* [Record.RenameFields](record-renamefields.md)
* [Record.ReorderFields](record-reorderfields.md)
* [Record.SelectFields](record-selectfields.md)
* [Table.RemoveColumns](table-removecolumns.md)
* [Table.RenameColumns](table-renamecolumns.md)
* [Table.ReorderColumns](table-reordercolumns.md)
* [Table.SelectColumns](table-selectcolumns.md)
* [Table.TransformColumns](table-transformcolumns.md)
