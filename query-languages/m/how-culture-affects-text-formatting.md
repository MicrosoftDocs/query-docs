---
title: How culture affects text formatting
description: Learn about how culture is related to the locale in which queries are authored and how you can change the default culture.
author: DougKlopfenstein
ms-author: dougklo
ms.date: 10/7/2024
ms.topic: reference
ms.subservice: m-background

---

# How culture affects text formatting

Different countries and language groups have different conventions for formatting different kinds of text, such as numbers, dates, and time. In Power Query, *culture* refers to the locale whose conventions are used to format this type of text in Power Query M. This locale is generally composed of the language and the country where the language is spoken, for example "en-US" for the English language spoken in the United States of America.

## Default culture

The default culture is set to the system locale (Windows, MacOS) of a particular document where your queries are first authored. For example, if you author your queries in Power Query Desktop, the default culture is defined by the locale set on your local computer. However, if you author your queries in the Power Query Online, the default culture is defined by the locale set on the online service. No matter where you author your query, if you move your query to a different location that uses a different default culture, your query still uses the culture of the original location.

To use the current default culture, no culture setting is required in your Power Query M code.

However, you can change the default culture in the Power Query settings dialog where you create the query. For example, if you are running Power Query from Excel:

1. In Power Query, select **File** > **Options and settings** > **Query options**.
1. Under **Current Workbook**, select **Regional Settings**.
1. Select the locale you want to use.

Other versions of Power Query work similarly. In general, within Power Query you select **Options**, which opens the **Options** dialog. Then select **Regional Settings** and select the locale you want to use.

## Invariant culture

The invariant culture is culture-insensitive; it's associated with the English language but not with any country or region. You specify the invariant culture by name by using an empty string ("") in functions that include the culture parameter.

Unlike culture-sensitive data, which is subject to change by user customization or by updates to the operating system, invariant culture data is stable over time and across installed cultures and can't be customized by users. This makes the invariant culture particularly useful for operations that require culture-independent results, such as formatting and parsing operations that persist formatted data, or sorting and ordering operations that require that data be displayed in a fixed order regardless of culture.

To use the invariant culture in Power Query M, use the blank text value (`""`) in the numeric functions that support culture, or (`Culture = ""`) in date and time functions that support culture.

## Related content

- [Standard date and time format strings](standard-date-and-time-format-strings.md)
- [Custom date and time format strings](custom-date-and-time-format-strings.md)
- [Standard numeric format strings](standard-numeric-format-strings.md)
- [Custom numeric format strings](custom-numeric-format-strings.md)
