import wegene

wegene.Configuration.o_auth_access_token = '<A valid token with proper scope>'

profile_id = ''
try:
    user = wegene.WeGeneUser().get_user()
    profile_id = user.profiles[0].id
    print profile_id
except Exception as e:
    print e.response_body

try:
    risk = wegene.Risk().get_risk(profile_id, 88)
    print risk
except Exception as e:
    print e.response_body

try:
    athletigen = wegene.Athletigen().get_athletigen(profile_id, 1487)
    print athletigen
except Exception as e:
    print e.response_body

try:
    haplogroups = wegene.Haplogroups().get_haplogroups(profile_id)
    print haplogroups
except Exception as e:
    print e.response_body

try:
    drug = wegene.Health().get_drug(profile_id, 1481)
    print drug
except Exception as e:
    print e.response_body

try:
    advice = wegene.Sport().get_advice(profile_id, 'man', 26, 174, 84, 'slimming')
    print advice.total_intake
except Exception as e:
    print e.response_body

try:
    allele = wegene.Allele().get_allele(profile_id, ['rs182549'])
    print allele
except Exception as e:
    print e.response_body
