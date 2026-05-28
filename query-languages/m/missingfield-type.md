---
description: "Learn more about: MissingField.Type"
title: "MissingField.Type"
ms.subservice: m-source
ms.topic: reference
---

# MissingField.Type

## About

Specifies the expected action for missing values in a row that contains columns less than expected.

## Allowed values

|Name|Value|Description|
|---|---|---|
|`MissingField.Error`|0|An optional parameter in record and table functions indicating that missing fields should result in an error. (This is the default parameter value.)|
|`MissingField.Ignore`|1|An optional parameter in record and table functions indicating that missing fields should be ignored.|
|`MissingField.UseNull`|2|An optional parameter in record and table functions indicating that missing fields should be included as null values.|
