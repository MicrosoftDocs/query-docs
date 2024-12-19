---
description: "Learn more about: USERCULTURE"
title: "USERCULTURE function (DAX)"
---
# USERCULTURE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

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

- When combined with the Field parameters feature in Power BI, USERCULTURE can be used to reliably translate dynamic visualization titles and captions when used in measure and row-level security (RLS) object expressions within the same model. However, expressions containing USERCULTURE called from outside the model, such as queries and live-connect report measures, should not be relied upon for correctly translated titles and captions.

- USERCULTURE returns the correct user locale when used in object expressions called from within the model such as measures, row-level security (RLS), and calculation items. However, it may not return the correct user locale when used in expressions from outside the model, such as queries and live-connect report measures.

- In Live-connect reports, USERCULTURE may not return the correct user locale when called from a report measure expression.

## Example

For the following expression,

```dax
FORMAT(TODAY(), "dddd", USERCULTURE())
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

## Related content

[Expression-based titles in Power BI](/power-bi/create-reports/desktop-conditional-format-visual-titles)
[USERNAME](username-function-dax.md)
[USERPRINCIPALNAME](userprincipalname-function-dax.md)
[USEROBJECTID](userobjectid-function-dax.md)
