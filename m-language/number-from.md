---
title: "Number.From | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f5106cf5-d925-48a3-b16a-2edc1bd61871
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.From
<code>Number.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number</code>

## About
Returns a <code>number</code> value from the given <code>value</code>. If the given <code>value</code> is <code>null</code>, <code>Number.From</code> returns <code>null</code>. If the given <code>value</code> is <code>number</code>, <code>value</code> is returned. Values of the following types can be converted to a <code>number</code> value: <ul> <li><code>text</code>: A <code>number</code> value from textual representation. Common text formats are handled ("15", "3,423.10", "5.0E-10"). See <code>Number.FromText</code> for details.</li> <li><code>logical</code>: 1 for <code>true</code>, 0 for <code>false</code>.</li> <li><code>datetime</code>: A double-precision floating-point number that contains an OLE Automation date equivalent.</li> <li><code>datetimezone</code>: A double-precision floating-point number that contains an OLE Automation date equivalent of the local date and time of <code>value</code>.</li> <li><code>date</code>: A double-precision floating-point number that contains an OLE Automation date equivalent.</li> <li><code>time</code>: Expressed in fractional days.</li> <li><code>duration</code>: Expressed in whole and fractional days.</li> </ul> If <code>value</code> is of any other type, an error is returned.

## Example 1
Get the <code>number</code> value of <code>"4"</code>.

<code>Number.From("4")</code>

<code>4</code>

## Example 2
Get the <code>number</code> value of <code>#datetime(2020, 3, 20, 6, 0, 0)</code>.

<code>Number.From(#datetime(2020, 3, 20, 6, 0, 0))</code>

<code>43910.25</code>

## Example 3
Get the <code>number</code> value of <code>"12.3%"</code>.

<code>Number.From("12.3%")</code>

<code>0.123</code>
