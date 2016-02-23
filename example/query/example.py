import wegene

wegene.Configuration.o_auth_access_token = '<A Valid Access Token with Proper Scope>'

profile_id = ''
try:
    user = wegene.User().get_user()
    profile_id = user.profiles[0].id
    print profile_id
except Exception as e:
    print e.response_body

try:
    drug = wegene.Health().get_drug(profile_id, 158)
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
