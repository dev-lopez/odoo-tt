from xmlrpc import client


url = 'https://lopezalexisl-odoo-tt-space-mission-v5-6828419.dev.odoo.com'
db = 'lopezalexisl-odoo-tt-space-mission-v5-6828419'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'space.ship', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)

spaceship_fields = models.execute_kw(db, uid, password,
                                  'space.ship', 'fields_get',
                                  [],{'attributes': ['string', 'type', 'required']})
print(spaceship_fields)

new_spaceship = models.execute_kw(db, uid, password,
                               'space.ship', 'create',
                               [
                                   {
                                       'name': 'Millenium Falcon',
                                       'type': 'millitary',
                                       'model': 'YT-1300F light freighter',
                                       'captain': 'Han Solo',
                                       'length': 114,
                                       'width': 94,
                                       'height': 26,
                                       'fuel_type': 'solid_fuel',
                                   }
                               ]
                               )
print(new_spaceship)