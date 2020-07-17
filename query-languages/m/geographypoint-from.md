---
title: "GeographyPoint.From | Microsoft Docs"
ms.date: 7/16/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# GeographyPoint.From
## Syntax

<pre>
GeographyPoint.From(<b>longitude</b> as number, <b>latitude</b> as number, optional <b>z</b> as nullable number, optional <b>m</b> as nullable number, optional <b>srid</b> as nullable number) as record
</pre>

## About
Creates a record structure representing a geography point from its constituent parts, such as longitude, latitude, and if present, elevation (Z) and measure (M). An optional spatial reference identifier (SRID) can be given if different from the default value (4326).
