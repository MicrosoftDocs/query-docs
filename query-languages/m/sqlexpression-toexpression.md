---
description: "Learn more about: SqlExpression.ToExpression"
title: "SqlExpression.ToExpression"
ms.date: 10/18/2021
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# SqlExpression.ToExpression

## Syntax

<pre>
SqlExpression.ToExpression(<b>sql</b> as text, <b>environment</b> as record) as text
</pre>

## About

Converts the provided `sql` query to M code, with the available identifiers defined by `environment`. This function is intended for internal use only.
