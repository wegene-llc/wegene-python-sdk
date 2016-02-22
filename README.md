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

Use `wegene.User().get_user()` to get user data

```python
profile_id = ''
try:
    user = wegene.User().get_user()
    profile_id = user.profiles[0].id
    print profile_id
except Exception as e:
    print e.response_body
```

#### Get Gene Allele Info

Use `wegene.Allele().get_allele(profile_id, locations)` to get allele data

```python
try:
    allele = wegene.Allele().get_allele(profile_id, ['rs182549'])
    print allele
except Exception as e:
    print e.response_body
```

#### Get Sport Advice

Use `wegene.Sport().get_advice(profile_id, sex, age, height, weight, health_target)` to get sport advice

```python
try:
    advice = wegene.Sport().get_advice(profile_id, 'male', 26, 174, 84, 'slimming')
    print advice.total_intake
except Exception as e:
    print e.response_body
```

#### Get Health Data

Use `wegene.Health().get_risk(profile_id, report_id)` to get health risk info

Use `wegene.Health().get_drug(profile_id, report_id)` to get drug response info

Use `wegene.Health().get_carrier(profile_id, report_id)` to get disease carrier info

```python
try:
    drug = wegene.Health().get_drug(profile_id, 158)
    print drug
except Exception as e:
    print e.response_body
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
