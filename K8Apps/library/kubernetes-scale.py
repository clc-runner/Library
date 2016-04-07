#!/usr/bin/python
from pip._vendor.requests.models import CONTENT_CHUNK_SIZE

HAS_HTTPLIB2 = True
try:
    import httplib2
except ImportError:
    HAS_HTTPLIB2 = False
    
import json
    
def main():

    module = AnsibleModule(
        argument_spec = dict(
            endpoint = dict(required=False, default='http://127.0.0.1:8080'),
            name = dict(required=True),
            namespace = dict(required=False, default="default"),
            replicas = dict(required=True),
            fail_fast = dict(required=False, default=True)
        )
    )

    if not HAS_HTTPLIB2:
        module.fail_json(msg="httplib2 is not installed")

    endpoint = module.params['endpoint']
    name = module.params['name']
    namespace = module.params['namespace']
    replicas = int(module.params['replicas'])
    apiVersion = 'v1'
    fail_fast = module.params['fail_fast']
    h = httplib2.Http()

    response, content = h.request(endpoint + '/api/' + apiVersion + 
            '/namespaces/' + namespace + '/replicationcontrollers/' + name)

    if response.status == 404 and fail_fast:
        module.fail_json(changed=False, msg='Replication controller not found.')
            
    if response.status == 404 and not fail_fast:
        module.exit_json(changed=False, content=content)
            
    model = json.loads(content)
    model['spec']['replicas'] = replicas
            
    response, content = h.request(endpoint + '/api/' + apiVersion + 
            '/namespaces/' + namespace + '/replicationcontrollers/' + name, 
                    method='PUT', headers={'Content-Type':'application/json'}, body=json.dumps(model))
        
    if response.status >= 400 and fail_fast:
        module.fail_json(changed=False, msg='Failed to scale replication controller.')

    module.exit_json(changed=True, content=content)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()