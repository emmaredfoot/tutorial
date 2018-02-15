SIMULATION = {
 'simulation': {
  'archetypes': {
   'spec': [
    {'lib': 'tut.agents', 'name': 'Storage'},
    {'lib': 'agents', 'name': 'NullInst'},
    {'lib': 'agents', 'name': 'NullRegion'},
   ],
  },
  'control': {'duration': 10, 'startmonth': 1, 'startyear': 2000},
  'facility': {'config': {'Storage': {
                            'throughput': 10,
                            'storage_time': 1,
                            'incommod': 'fuel',
                            'outcommod': 'stored_fuel',
                            }},
                             'name': 'OneFacility'},
  'region': {
   'config': {'NullRegion': None},
   'institution': {
    'config': {'NullInst': None},
    'initialfacilitylist': {'entry': {'number': 1, 'prototype': 'OneFacility'}},
    'name': 'OneInst',
   },
   'name': 'OneRegion',
  },
 },
}
