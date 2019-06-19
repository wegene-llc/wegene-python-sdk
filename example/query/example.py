import wegene

wegene.Configuration.BASE_URI = 'https://api.wegene.com'
wegene.Configuration.o_auth_access_token = '<A Valid Access Token with Proper Scope>'

profile_id = ''
try:
    user = wegene.WeGeneUser().get_user()
    profile_id = user.profiles[0].id
    print(profile_id)
    print(user.profiles[0].format)
    print(user.profiles[0].name)
except Exception as e:
    print(e.response_body)

try:
    risk = wegene.Risk().get_risk(profile_id, 88)
    print(risk.caseid)
    print(risk.risk)
    print(risk.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    athletigen = wegene.Athletigen().get_athletigen(profile_id, 1487)
    print(athletigen.caseid)
    print(athletigen.rank)
    print(athletigen.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    skin = wegene.Skin().get_skin(profile_id, 1522)
    print(skin.caseid)
    print(skin.rank)
    print(skin.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    psychology = wegene.Psychology().get_psychology(profile_id, 1557)
    print(psychology.caseid)
    print(psychology.rank)
    print(psychology.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    ancestry = wegene.Ancestry().get_ancestry(profile_id)
    print(ancestry.block.chinese_nation)
    print(ancestry.area.han_southern)
except Exception as e:
    print(e.response_body)

try:
    haplogroups = wegene.Haplogroups().get_haplogroups(profile_id)
    print(haplogroups.y)
    print(haplogroups.mt)
except Exception as e:
    print(e.response_body)

try:
    demographics = wegene.Demographics().get_demographics(profile_id)
    print(demographics.surname)
    print(demographics.population)
except Exception as e:
    print(e.response_body)

try:
    drug = wegene.Health().get_drug(profile_id, 1481)
    print(drug.caseid)
    print(drug.tsummary)
    print(drug.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    metabolism = wegene.Health().get_metabolism(profile_id, 5)
    print(metabolism.caseid)
    print(drug.rank)
    print(metabolism.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    carrier = wegene.Health().get_carrier(profile_id, 184)
    print(carrier.caseid)
    print(carrier.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    traits = wegene.Health().get_traits(profile_id, 34)
    print(traits.caseid)
    print(traits.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    allele = wegene.Allele().get_allele(profile_id, ['rs671'])
    print(allele)
except Exception as e:
    print(e.response_body)
