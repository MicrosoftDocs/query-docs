---
description: "Learn more about: USERCULTURE"
title: "USERCULTURE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 08/31/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# USERCULTURE
  
Returns the locale \(language code-country code) for the current user, determined by the operating system, browser settings, or Power BI service.  

**Note:** This function is currently supported in Power BI Premium per capacity, Power BI Premium per user, and Power BI Embedded only.
  
## Syntax  
  
```dax
USERCULTURE()
```
  
### Parameters  
  
This expression has no parameters.
  
## Return value

Locale as a string.
  
## Remarks

- In the Power BI service, locale is determined by **Settings** > **Language** > **Language Settings**. The default is determined by the user's browser language setting.

- When used in calculated table and calculated column expressions, the result may differ depending on whether the table is in DirectQuery or Import mode. When in DirectQuery mode, the result is determined by the language (locale) specified in Language Settings in the Power BI service. The default in Language Settings specifies locale is determined by the user's browser language setting, which means the same calculated table or column can return different results depending on the browser language settings for each user. When in Import mode, the result is statically determined during refresh and will not vary at query time. For managed refreshes, such as scheduled or interactive, locale is not based on the user’s browser language setting but instead uses an invariant locale. The invariant locale, however, can be overridden by using the XMLA endpoint to specify a custom locale.

## Example

For the following expression,

```dax
FORMAT(TODAY(), “dddd”, USERCULTURE())
```

Depending on the language setting for the current user, :::no-loc text="USERCULTURE"::: returns the current day, for example:

|Locale  | Formatted weekday |
|---------|---------|
|de-DE     |  :::no-loc text="Dienstag":::|
|en-US     |  :::no-loc text="Tuesday":::|
|es-ES_tradnl     |  :::no-loc text="martes":::|
|eu-ES     |  :::no-loc text="asteartea":::|
|it-IT     |  :::no-loc text="martedì":::|
|nl-NL     |  :::no-loc text="dinsdag":::|
|pl-PL     |  :::no-loc text="wtorek":::|
|ro-RO     |  :::no-loc text="marți":::|
|ru-RU     |  :::no-loc text="вторник":::|
|uk-UA     |  :::no-loc text="вівторок":::|

## See also

[Expression-based titles in Power BI](/power-bi/create-reports/desktop-conditional-format-visual-titles)  
[USERNAME](username-function-dax.md)  
[USERPRINCIPALNAME](userprincipalname-function-dax.md)  
[USEROBJECTID](userobjectid-function-dax.md)  
