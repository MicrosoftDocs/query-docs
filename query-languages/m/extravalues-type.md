---
description: "Learn more about: ExtraValues.Type"
title: "ExtraValues.Type"
ms.subservice: m-source
ms.topic: reference
---

# ExtraValues.Type

## About

Specifies the expected action for extra values in a row that contains columns more than expected.

## Allowed values

|Name|Value|Description|
|---|---|---|
|`ExtraValues.List`|0|If the splitter function returns more columns than the table expects, they should be collected into a list.|
|`ExtraValues.Error`|1|If the splitter function returns more columns than the table expects, an error should be raised.|
|`ExtraValues.Ignore`|2|If the splitter function returns more columns than the table expects, they should be ignored.|
