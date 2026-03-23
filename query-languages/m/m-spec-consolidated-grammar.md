---
title: M Language Consolidated Grammar 
description: Describes all of the grammar associated with the Power Query M formula language
ms.topic: language-reference
ms.date: 01/29/2025
ms.custom: "nonautomated-date"
ms.subservice: m-specification
---

# Consolidated Grammar

## Lexical grammar

_lexical-unit:<br/>
      lexical-elements<sub>opt</sub><br/>
lexical-elements:<br/>
      lexical-element lexical-elements<sub>opt</sub><br/>
lexical-element:<br/>
      whitespace<br/>
      token<br/>
      comment_

### White space

_whitespace:_<br/>
      Any character with Unicode class Zs<br/>
      Horizontal tab character (`U+0009`)<br/>
      Vertical tab character (`U+000B`)<br/>
      Form feed character (`U+000C`)<br/>
      Carriage return character (`U+000D`) followed by line feed character (`U+000A`)
      _new-line-character<br/>
new-line-character:_<br/>
      Carriage return character (`U+000D`)<br/>
      Line feed character (`U+000A`)<br/>
      Next line character (`U+0085`)<br/>
      Line separator character (`U+2028`)<br/>
      Paragraph separator character (`U+2029`)

### Comment

_comment:<br/>
      single-line-comment<br/>
      delimited-comment</em><br/> 
single-line-comment:_<br/>
      `//`  _single-line-comment-characters<sub>opt</sub><br/>
single-line-comment-characters:<br/>
      single-line-comment-character  single-line-comment-characters<sub>opt</sub><br/> 
single-line-comment-character:_<br/>
      Any Unicode character except a _new-line-character<br/>
delimited-comment:_<br/>
      `/*` _delimited-comment-text<sub>opt</sub>  asterisks_  `/`<br/>
_delimited-comment-text:<br/>
      delimited-comment-section delimited-comment-text<sub>opt</sub><br/>
delimited-comment-section:_<br/>
      `/`<br/>
      _asterisks<sub>opt</sub>  not-slash-or-asterisk<br/> 
asterisks:_ <br/>
      `*` _asterisks<sub>opt</sub><br/> 
not-slash-or-asterisk:_<br/>
      Any Unicode character except `*` or `/`

### Tokens

_token:<br/>
      identifier<br/>
      keyword<br/>
      literal<br/>
      operator-or-punctuator_

### Character escape sequences

_character-escape-sequence:_<br/>
      `#(`  _escape-sequence-list_  `)`<br/>
_escape-sequence-list:<br/>
      single-escape-sequence<br/>
      escape-sequence-list_  `,`  _single-escape-sequence<br/>
single-escape-sequence:<br/>
      long-unicode-escape-sequence<br/>
      short-unicode-escape-sequence<br/>
      control-character-escape-sequence<br/>
      escape-escape<br/>
long-unicode-escape-sequence:<br/>
      hex-digit  hex-digit  hex-digit  hex-digit  hex-digit  hex-digit  hex-digit  hex-digit<br/>
short-unicode-escape-sequence:<br/>
      hex-digit  hex-digit  hex-digit  hex-digit<br/>
control-character-escape-sequence:<br/>
      control-character<br/>
control-character:_<br/>
      `cr`<br/>
      `lf`<br/>
      `tab`<br/>
_escape-escape:_<br/>
      `#`

### Literals

_literal:<br/>
      logical-literal<br/>
      number-literal<br/>
      text-literal<br/>
      null-literal<br/>
      verbatim-literal<br/>
logical-literal:<br/>
      `true`<br/>
      `false`<br/>
number-literal:<br/>
      decimal-number-literal<br/>
      hexadecimal-number-literal<br/>
decimal-digits:<br/>
      decimal-digit decimal-digits<sub>opt</sub><br/>
decimal-digit:_  one of<br/>
      `0  1  2  3  4  5  6  7  8  9`<br/>
_hexadecimal-number-literal:_<br/>
      `0x`  _hex-digits_<br/>
      `0X`  _hex-digits<br/>
hex-digits:<br/>
      hex-digit hex-digits<sub>opt</sub><br/>
hex-digit:_  one of<br/>
      `0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  a  b  c  d e  f`<br/>
_decimal-number-literal:<br/> 
      decimal-digits_  `.`  _decimal-digits  exponent-part<sub>opt</sub>_<br/>
      `.`  _decimal-digits  exponent-part<sub>opt</sub><br/>
      decimal-digits  exponent-part<sub>opt</sub><br/>
exponent-part:_<br/>
      `e`  _sign<sub>opt</sub>  decimal-digits_<br/>
      `E`  _sign<sub>opt</sub>  decimal-digits<br/> sign:_  one of<br/> 
      `+  -`<br/>
_text-literal:_<br/> 
      `"`  _text-literal-characters<sub>opt</sub>_  `"`<br/>
_text-literal-characters:<br/>
      text-literal-character  text-literal-characters<sub>opt</sub><br/>
text-literal-character:<br/>
      single-text-character<br/>
      character-escape-sequence<br/>
      double-quote-escape-sequence<br/>
single-text-character:_<br/>
      Any character except `"` (`U+0022`) or `#` (`U+0023`) followed by `(` (`U+0028`)<br/>
_double-quote-escape-sequence:_<br/>
      `""` (`U+0022`, `U+0022`)<br/>
_null-literal:_<br/>
      `null`<br/>
_verbatim-literal:_<br/>
      `#!"` _text-literal-characters<sub>opt</sub>_ `"`

### Identifiers

_identifier:<br/>
      regular-identifier<br/>
      quoted-identifier<br/>
regular-identifier:<br/>
      available-identifier<br/>
      available-identifier  dot-character  regular-identifier<br/>
available-identifier:_<br/>
      A _keyword-or-identifier_ that is not a _keyword<br/>
keyword-or-identifier:<br/>
      letter-character<br/>
      underscore-character<br/>
      identifier-start-character 
identifier-part-characters<br/>
identifier-start-character:<br/>
      letter-character<br/>
      underscore-character<br/>
identifier-part-characters:<br/>
      identifier-part-character  identifier-part-characters<sub>opt</sub><br/>
identifier-part-character:<br/>
      letter-character<br/>
      decimal-digit-character<br/>
      underscore-character<br/>
      connecting-character<br/>
      combining-character<br/>
      formatting-character<br/>
generalized-identifier:<br/>
      generalized-identifier-part<br/>
      generalized-identifier_ separated only by blanks (`U+0020`) _generalized-identifier-part<br/>
generalized-identifier-part:<br/>
      generalized-identifier-segment<br/>
      decimal-digit-character generalized-identifier-segment<br/>
generalized-identifier-segment:<br/>
      keyword-or-identifier<br/>
      keyword-or-identifier dot-character  keyword-or-identifier<br/>
dot-character:_<br/>
      `.`  (`U+002E`)<br/>
_underscore-character:_<br/>
      `_`  (`U+005F`)<br/>
letter-character:_<br/>
      A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nl<br/>
_combining-character:_<br/>
      A Unicode character of classes Mn or Mc<br/>
_decimal-digit-character:_<br/>
      A Unicode character of the class Nd<br/>
_connecting-character:_<br/>
      A Unicode character of the class Pc<br/>
_formatting-character:_<br/>
      A Unicode character of the class Cf<br/>
_quoted-identifier:_<br/>
      `#"`  _text-literal-characters<sub>opt</sub>_  `"`

### Keywords and predefined identifiers

Predefined identifiers and keywords cannot be redefined. A quoted identifier can be used to handle identifiers that would otherwise collide with predefined identifiers or keywords.

_keyword:_  one of</br>
      `and as each else error false if in is let meta not null or otherwise`<br/>
      `section shared then true try type #binary #date #datetime`<br/>
      `#datetimezone #duration #infinity #nan #sections #shared #table #time`

### Operators and punctuators

_operator-or-punctuator:_  one of<br/>
      `, ; = < <= > >= <> + - * / & ( ) [ ] { } @ ? ?? => .. ...`

## Syntactic grammar

### Documents

_document:<br/>
      section-document<br/>
      expression-document_

### Section Documents

_section-document:<br/>
      section<br/>
section:<br/>
      literal-attributes<sub>opt</sub>_  `section`  _section-name_  `;`  _section-members<sub>opt</sub><br/>
section-name:<br/>
      identifier<br/>
section-members:<br/>
      section-member section-members<sub>opt</sub><br/>
section-member:<br/>
      literal-attributes<sub>opt</sub>  shared<sub>opt</sub>  section-member-name_  `=`  _expression_  `;`<br/>
_section-member-name:<br/>
      identifier_

### Expression Documents

#### Expressions

_expression-document:<br/>
      expression<br/>
expression:<br/>
      logical-or-expression</br>
      each-expression<br/>
      function-expression<br/>
      let-expression<br/>
      if-expression<br/>
      error-raising-expression<br/>
      error-handling-expression_

#### Logical expressions

_logical-or-expression:<br/>
      logical-and-expression<br/>
      logical-and-expression_  `or`  _logical-or-expression<br/>
logical-and-expression:<br/>
      is-expression<br/>
      logical-and-expression_  `and`  _is-expression_

#### Is expression

_is-expression:<br/>
      as-expression<br/>
      is-expression_ `is`  _primitive-or-nullable-primitive-type_

#### As expression

_as-expression:<br/>
      equality-expression<br/>
      as-expression_  `as`  _primitive-or-nullable-primitive-type_

#### Equality expression

_equality-expression:<br/>
      relational-expression<br/>
      relational-expression_  `=`  _equality-expression<br/>
      relational-expression_  `<>`  _equality-expression_

#### Relational expression

_relational-expression:<br/>
      additive-expression<br/>
      additive-expression_  `<`  _relational-expression<br/>
      additive-expression_  `>`  _relational-expression<br/>
      additive-expression_  `<=`  _relational-expression<br/>
      additive-expression_  `>=`  _relational-expression_

#### Arithmetic expressions

_additive-expression:<br/>
      multiplicative-expression<br/>
      multiplicative-expression_  `+`  _additive-expression<br/>
      multiplicative-expression_  `-`  _additive-expression<br/>
      multiplicative-expression_  `&`  _additive-expression<br/>
_multiplicative-expression:<br/>
      metadata-expression<br/>
      metadata-expression_  `*`  _multiplicative-expression<br/>
      metadata-expression_  `/`  _multiplicative-expression_

#### Metadata expression

_metadata-expression:<br/>
      unary-expression<br/>
      unary-expression_  `meta`  _unary-expression_

#### Unary expression

_unary-expression:<br/>
      type-expression_<br/>
      `+`  _unary-expression_<br/>
      `-`  _unary-expression_<br/>
      `not`  _unary-expression_

#### Primary expression

_primary-expression:<br/>
      literal-expression<br/>
      list-expression<br/>
      record-expression<br/>
      identifier-expression<br/>
      section-access-expression<br/>
      parenthesized-expression<br/>
      field-access-expression<br/>
      item-access-expression<br/>
      invoke-expression<br/>
      not-implemented-expression_

#### Literal expression

_literal-expression:<br/>
      literal_

#### Identifier expression

_identifier-expression:<br/>
      identifier-reference<br/>
identifier-reference:<br/>
      exclusive-identifier-reference<br/>
      inclusive-identifier-reference<br/> 
exclusive-identifier-reference:<br/>
      identifier<br/>
inclusive-identifier-reference:_<br/> 
      `@`  _identifier_

#### Section-access expression

_section-access-expression:<br/>
      identifier_ `!` _identifier_

#### Parenthesized expression

_parenthesized-expression:_<br/>
      `(`  _expression_  `)`

#### Not-implemented expression

_not-implemented-expression:_<br/>
      `...`

#### Invoke expression

_invoke-expression:<br/>
      primary-expression_  `(`  _argument-list<sub>opt</sub>_  `)`<br/>
_argument-list:<br/>
      expression<br/>
      expression_  `,`   _argument-list_

#### List expression

_list-expression:_<br/>
      `{`  _item-list<sub>opt</sub>_  `}`<br/>
_item-list:<br/>
      item<br/>
      item_  `,`  _item-list<br/>
item:<br/>
      expression<br/>
      expression_  `..`  _expression_

#### Record expression

_record-expression:_<br/>
      `[`  _field-list<sub>opt<sub>_  `]`<br/>
_field-list:<br/>
      field<br/>
      field_  `,`  _field-list<br/>
field:<br/>
      field-name_  `=`  _expression<br/>
field-name:<br/>
      generalized-identifier<br/>
      quoted-identifier_<br/>

#### Item access expression

_item-access-expression:<br/>
      item-selection<br/>
      optional-item-selection<br/>
item-selection:</br>
      primary-expression_  `{`  _item-selector_  `}`<br/>
_optional-item-selection:<br/>
      primary-expression_  `{`  _item-selector_  `} ?`<br/>
_item-selector:<br/>
      expression_

#### Field access expressions

_field-access-expression:<br/>
      field-selection<br/>
      implicit-target-field-selection<br/>
      projection<br/>
      implicit-target-projection<br/>
field-selection:<br/>
      primary-expression  field-selector<br/>
field-selector:<br/>
      required-field-selector<br/>
      optional-field-selector<br/>
required-field-selector:_<br/>
      `[`   _field-name_  `]`<br/>
_optional-field-selector:_<br/>
      `[`   _field-name_  `] ?`<br/>
implicit-target-field-selection:<br/>
      field-selector<br/>
projection:<br/>
      primary-expression  required-projection<br/>
      primary-expression  optional-projection<br/>
required-projection:_<br/>
      `[` _required-selector-list_ `]`<br/>
_optional-projection:_<br/>
      `[` _required-selector-list_ `] ?`<br/>
_required-selector-list:<br/>
      required-field-selector<br/>
      required-field-selector_ `,`  _required-selector-list<br/>
implicit-target-projection:<br/>
      required-projection<br/>
      optional-projection_

#### Function expression

_function-expression:_<br/>
      `(`  _parameter-list<sub>opt</sub>_  `)`  _return-type<sub>opt</sub>_  `=>`  _function-body<br/>
function-body:<br/>
      expression<br/>
parameter-list:<br/>
      fixed-parameter-list<br/>
      fixed-parameter-list_  `,`  _optional-parameter-list<br/>
      optional-parameter-list<br/>
fixed-parameter-list:<br/>
      parameter<br/>
      parameter_  `,`  _fixed-parameter-list<br/>
parameter:<br/>
      parameter-name parameter-type<sub>opt</sub><br/>
parameter-name:<br/>
      identifier<br/>
parameter-type:<br/>
      primitive-or-nullable-primitive-type-assertion<br/>
return-type:<br/>
      primitive-or-nullable-primitive-type-assertion<br/>
primitive-or-nullable-primitive-type-assertion:_<br/>
      `as`  _primitive-or-nullable-primitive-type<br/>
optional-parameter-list:<br/>
      optional-parameter<br/>
      optional-parameter_  `,`  _optional-parameter-list<br/>
optional-parameter:_<br/>
      `optional`  _parameter_

#### Each expression

_each-expression:_<br/>
      `each` _each-expression-body<br/>
each-expression-body:<br/>
      function-body_

#### Let expression

_let-expression:_<br/>
      `let`  _variable-list_  `in`  _expression<br/>
variable-list:<br/>
      variable<br/>
      variable_  `,`  _variable-list<br/>
variable:<br/>
      variable-name_  `=`  _expression<br/>
variable-name:<br/>
      identifier_

#### If expression

_if-expression:_<br/>
      `if` _if-condition_  `then`  _true-expression_  `else`  _false-expression<br/>
if-condition:<br/>
      expression<br/> 
true-expression:<br/>
      expression<br/>
false-expression:<br/>
      expression_

#### Type expression

_type-expression:<br/>
      primary-expression_<br/>
      `type`  _primary-type<br/>
type:<br/>
      primary-expression<br/>
      primary-type<br/>
primary-type:<br/>
      primitive-or-nullable-primitive-type<br/>
      record-type<br/>
      list-type<br/>
      function-type<br/>
      table-type<br/>
      nullable-type_<br />
_primitive-or-nullable-primitive-type:_<br/>
      `nullable`_<sub>opt</sub> primitive-type_<br />
_primitive-type:_ one of<br/>
      `any anynonnull binary date datetime datetimezone duration function list logical`<br/>
      `none null number record table text time type`<br/>
_record-type:_<br/>
      `[`  _open-record-marker_  `]`<br/>
      `[`   _field-specification-list<sub>opt</sub>_  `]`<br/>
      `[`   _field-specification-list_  `,`  _open-record-marker_  `]` <br/>
_field-specification-list:<br/>
      field-specification<br/>
      field-specification_
  `,`  _field-specification-list<br/>
field-specification:_<br/>
      `optional`_<sub>opt</sub> field-name field-type-specification<sub>opt</sub><br/>
field-type-specification:_<br/>
      `=` _field-type<br/>
field-type:<br/>
      type<br/>
open-record-marker:_<br/>
      `...`<br/>
_list-type:_<br/>
      `{`   _item-type_   `}`<br/>
_item-type:<br/>
      type<br/>
function-type:_<br/>
      `function (`  _parameter-specification-list<sub>opt</sub>_  `)`  _return-type<br/>
parameter-specification-list:<br/>
      required-parameter-specification-list<br/>
      required-parameter-specification-list_  `,`  _optional-parameter-specification-list<br/>
      optional-parameter-specification-list<br/>
required-parameter-specification-list:<br/>
      required-parameter-specification<br/>
      required-parameter-specification_  `,`  _required-parameter-specification-list<br/>
required-parameter-specification:<br/>
      parameter-specification<br/>
optional-parameter-specification-list:<br/>
      optional-parameter-specification<br/>
      optional-parameter-specification_  `,`  _optional-parameter-specification-list<br/>
optional-parameter-specification:_<br/>
      `optional` _parameter-specification<br/> 
parameter-specification:<br/>
      parameter-name parameter-type<br/>
parameter-type:<br/>
      type-assertion<br/>
type-assertion:_<br/>
      `as` _type<br/>
table-type:_<br/>
      `table`  _row-type<br/>
row-type:_<br/>
      `[`   _field-specification-list_<sub>opt</sub>  `]`<br/>
_nullable-type:_<br/>
      `nullable`  _type_

#### Error raising expression

_error-raising-expression:_<br/>
      `error`  expression_

#### Error handling expression

_error-handling-expression:_<br/>
      `try` _protected-expression 
error-handler<sub>opt</sub><br/>
protected-expression:<br/>
      expression<br/>
_error-handler:_<br/>
      otherwise-clause<br/>
      catch-clause<br/>
otherwise-clause:_<br/>
      `otherwise` _default-expression_<br/>
_default-expression_:<br/>
      _expression_<br/>
_catch-clause:_<br/>
      `catch` _catch-function_<br/>
_catch-function:_<br/>
      `(`_parameter-name<sub>opt</sub>_`)` `=>` _function-body_<br/>

### Literal Attributes

_literal-attributes:<br/>
      record-literal<br/>
record-literal:_<br/>
      `[` _literal-field-list<sub>opt</sub>_ `]`<br/>
_literal-field-list:<br/>
      literal-field<br/>
      literal-field_ `,` _literal-field-list<br/>
literal-field:<br/>
      field-name_ `=` _any-literal<br/>
list-literal:_<br/>
      `{` _literal-item-list<sub>opt</sub>_ `}`<br/>
_literal-item-list:<br/>
      any-literal<br/>
      any-literal_ `,` _literal-item-list<br/>
any-literal:<br/>
      record-literal<br/>
      list-literal<br/>
      logical-literal<br/>
      number-literal<br/>
      text-literal<br/>
      null-literal_
