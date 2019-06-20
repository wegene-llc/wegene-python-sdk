import wegene

wegene.Configuration.BASE_URI = 'https://api.wegene.com'
wegene.Configuration.o_auth_access_token = '<>'

profile_id = ''
try:
    user = wegene.WeGeneUser().get_user()
    profile_id = user.profiles[0].id
    print('--- Profile ---')
    print(profile_id)
    print(user.profiles[0].format)
    print(user.profiles[0].name)
except Exception as e:
    print(e.response_body)

try:
    risk = wegene.Risk().get_risk(profile_id, 88)
    print('--- Risk ---')
    print(risk.caseid)
    print(risk.description)
    print(risk.risk)
    print(risk.genotypes.data[0].rsid)
except Exception as e:
    print(e.response_body)

try:
    athletigen = wegene.Athletigen().get_athletigen(profile_id, 1487)
    print('--- Athletigen ---')
    print(athletigen.caseid)
    print(athletigen.description)
    print(athletigen.rank)
    print(athletigen.genotypes.data[0].rsid)
    print(athletigen.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)

try:
    skin = wegene.Skin().get_skin(profile_id, 1522)
    print('--- Skin ---')
    print(skin.caseid)
    print(skin.description)
    print(skin.rank)
    print(skin.genotypes.data[0].rsid)
    print(skin.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)

try:
    psychology = wegene.Psychology().get_psychology(profile_id, 1557)
    print('--- Psychology ---')
    print(psychology.caseid)
    print(psychology.description)
    print(psychology.rank)
    print(psychology.genotypes.data[0].rsid)
    print(psychology.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)

try:
    ancestry = wegene.Ancestry().get_ancestry(profile_id)
    print('--- Ancestry Composition ---')
    print(ancestry.block.chinese_nation)
    print(ancestry.area.han_southern)
except Exception as e:
    print(e.response_body)

try:
    haplogroups = wegene.Haplogroups().get_haplogroups(profile_id)
    print('--- Haplogroups ---')
    print(haplogroups.y)
    print(haplogroups.mt)
except Exception as e:
    print(e.response_body)

try:
    demographics = wegene.Demographics().get_demographics(profile_id)
    print('--- Demographics ---')
    print(demographics.surname)
    print(demographics.population)
except Exception as e:
    print(e.response_body)

try:
    drug = wegene.Health().get_drug(profile_id, 1481)
    print('--- Drug ---')
    print(drug.caseid)
    print(drug.description)
    print(drug.tsummary)
    print(drug.genotypes.data[0].rsid)
    print(drug.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)

try:
    metabolism = wegene.Health().get_metabolism(profile_id, 5)
    print('--- Metabolism ---')
    print(metabolism.caseid)
    print(metabolism.description)
    print(metabolism.rank)
    print(metabolism.genotypes.data[0].rsid)
    print(metabolism.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)

try:
    carrier = wegene.Health().get_carrier(profile_id, 184)
    print('--- Carrier ---')
    print(carrier.caseid)
    print(carrier.description)
    print(carrier.genotypes.data[0].rsid)
    for allele in carrier.genotypes.data:
        print(allele.genotype)
        print(allele.tsummary)
except Exception as e:
    print(e.response_body)

try:
    traits = wegene.Health().get_traits(profile_id, 34)
    print('--- Traits ---')
    print(traits.caseid)
    print(traits.description)
    print(traits.tsummary)
    print(traits.genotypes.data[0].rsid)
    print(traits.genotypes.data[0].genotype)
except Exception as e:
    print(e.response_body)

try:
    allele = wegene.Allele().get_allele(profile_id, ['rs671'])
    print('--- Allele ---')
    print(allele['RS671'])
except Exception as e:
    print(e.response_body)
