---
description: "Learn more about: ExtraValues.Type"
title: "ExtraValues.Type | Microsoft Docs"
ms.date: 5/4/2022
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# ExtraValues.Type

## Definition

Specifies the expected action for extra values in a row that contains columns less than expected.

## Fields

|Field|Value|Description|
| ------- | --- | ----------- |
|**Error**|1| If the splitter function returns more columns than the table expects, an error should be raised.|
|**Ignore**|2|If the splitter function returns more columns than the table expects, they should be ignored.|
|**List**|0|If the splitter function returns more columns than the table expects, they should be collected into a list.|

## See also

* [Table.FromList](table-fromlist.md)
