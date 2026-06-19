---
description: "Learn more about: TextEncoding.Type"
title: "TextEncoding.Type"
ms.subservice: m-source
ms.topic: reference
---

# TextEncoding.Type

## About

Specifies the text encoding type.

## Allowed values

|Name|Value|Description|
|---|---|---|
|`TextEncoding.Utf16`|1200|Use to choose the UTF16 little endian binary form.|
|`TextEncoding.Unicode`|1200|Use to choose the UTF16 little endian binary form.|
|`TextEncoding.BigEndianUnicode`|1201|Use to choose the UTF16 big endian binary form.|
|`TextEncoding.Windows`|1252|Use to choose the Windows binary form.|
|`TextEncoding.Ascii`|20127|Use to choose the ASCII binary form.|
|`TextEncoding.Utf8`|65001|Use to choose the UTF8 binary form.|

## More information

Any text encoding parameter should accept any of the Windows code pages by number. You don't need an M enumeration for it.

## Related content

* [Text functions](text-functions.md)
