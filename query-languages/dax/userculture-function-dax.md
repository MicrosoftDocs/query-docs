---
description: "Learn more about: USERCULTURE"
title: "USERCULTURE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 08/23/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# USERCULTURE
  
Returns the locale \(language code-country code) for the current user, determined by operating system or browser settings.  

**Note:** This function is currently supported in Power BI Desktop, Power BI Premium per capacity, Power BI Premium per user, and Power BI Embedded only.
  
## Syntax  
  
```dax
USERCULTURE()
```
  
### Parameters  
  
This expression has no parameters.
  
## Return value

Locale as a string.
  
## Remarks

- In Power BI service, locale is determined by **Settings** > **Language** > **Language Settings**. By default, locale is determined by the user browser settings.

- In Power BI Desktop, locale is determined by **File** > **Options and settings** > **Options** > **Regional Settings** > **Application language**. By default, locale is determined by the computer operating system language settings.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query,

```dax
EVALUATE
{ 
    USERCULTURE()
}
```

Returns,

|Value  |
|---------|
|en-US     |
