# wegene-python-sdk

Python SDK for [WeGene](https://www.wegene.com)

## Installation

    $ pip install wegene

## Usage

#### Set Access Token

To query data from WeGene, one need a valid OAuth2 access token authorized by
the user.


```python
import wegene
wegene.Configuration.o_auth_access_token = '<A Valid Access Token with Proper Scope>'
```

#### Get Basic User Info

Use `wegene.WeGeneUser().get_user()` to get user data

```python
profile_id = ''
try:
    user = wegene.WeGeneUser().get_user()
    print(user.profiles[0].id)
    print(user.profiles[0].format)
    print(user.profiles[0].name)
except Exception as e:
    print(e.response_body)
```

#### Get Gene Allele Info

Use `wegene.Allele().get_allele(profile_id, locations)` to get allele data

```python
try:
    allele = wegene.Allele().get_allele(profile_id, ['rs182549'])
    print(allele)
except Exception as e:
    print(e.response_body)
```

#### Get Athletigen

Use `wegene.Athletigen().get_athletigen(profile_id, report_id)` to get athletigen data

```python
try:
    athletigen = wegene.Athletigen().get_athletigen(profile_id, 1487)
    print(athletigen.caseid)
    print(athletigen.description)
    print(athletigen.rank)
    print(athletigen.genotypes.data[0].rsid)
    print(athletigen.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)
```

#### Get Skin

Use `wegene.Skin().get_skin(profile_id, report_id)` to get skin data

```python
try:
    skin = wegene.Skin().get_skin(profile_id, 1522)
    print(skin.caseid)
    print(skin.description)
    print(skin.rank)
    print(skin.genotypes.data[0].rsid)
    print(skin.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)
```

#### Get Psychology

Use `wegene.Psychology().get_psychology(profile_id, report_id)` to get psychology data

```python
try:
    psychology = wegene.Psychology().get_psychology(profile_id, 1557)
    print(psychology.caseid)
    print(psychology.description)
    print(psychology.rank)
    print(psychology.genotypes.data[0].rsid)
    print(psychology.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)
```

#### Get Health Risk

Use `wegene.Risk().get_risk(profile_id, report_id)` to get health risk data

```python
try:
    risk = wegene.Risk().get_risk(profile_id, 88)
    print(risk.caseid)
    print(risk.description)
    print(risk.risk)
    print(risk.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)
```

#### Get Metabolism/Traits/Drug/Carrier Report

Use `wegene.Health().get_metabolism(profile_id, report_id)` to get health metabolism info

Use `wegene.Health().get_traits(profile_id, report_id)` to get genetic traits info

Use `wegene.Health().get_drug(profile_id, report_id)` to get drug response info

Use `wegene.Health().get_carrier(profile_id, report_id)` to get disease carrier info

```python
try:
    carrier = wegene.Health().get_drug(profile_id, 184)
    print(carrier.caseid)
    print(carrier.description)
    print(carrier.genotypes.data[0].rsid)
    for allele in carrier.genotypes.data:
        print(allele.genotype)
        print(allele.tsummary)
except Exception as e:
    print(e.response_body)
```

#### Get Ancestry Composition

Use `wegene.Ancestry().get_ancestry(profile_id)` to get user ancestry composition

```python
try:
    ancestry = wegene.Ancestry().get_ancestry(profile_id)
    print(ancestry.block.chinese_nation)
    print(ancestry.area.han_southern)
except Exception as e:
    print(e.response_body)
```

#### Get Haplogroups

Use `wegene.Haplogroups().get_haplogroups(profile_id)` to get user haplogroups

```python
try:
    haplogroups = wegene.Haplogroups().get_haplogroups(profile_id)
    print(haplogroups.y)
    print(haplogroups.mt)
except Exception as e:
    print(e.response_body)
```

#### Get Demographics

Use `wegene.Demographics().get_demographics(profile_id)` to get user demographics

```python
try:
    demographics = wegene.Demographics().get_demographics(profile_id)
    print(demographics.surname)
    print(demographics.population)
except Exception as e:
    print(e.response_body)
```

## Documentation
  - [Full WeGene API Document](https://api.wegene.com/docs/)


## Credits
  - [Eddie Wu](https://xraywu.github.io)

## Thanks
  - The SDK is modified on top of the code auto-generated using [APIMATIC](https://apimatic.io). Huge thanks to the team as this is a real life saver!!

## License

(The MIT License)

Copyright (c) 2016 Eddie Wu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
