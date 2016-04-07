#!/usr/bin/python
from pip._vendor.requests.models import CONTENT_CHUNK_SIZE

HAS_HTTPLIB2 = True
try:
    import httplib2
except ImportError:
    HAS_HTTPLIB2 = False

import json

K8S_TYPE = {
    'node' : 'nodes'
}

def main():

    module = AnsibleModule(
        argument_spec = dict(
            endpoint = dict(required=False, default='http://127.0.0.1:8080'),
            state = dict(required=False, default='present'),
            model = dict(required=True)
        )
    )

    if not HAS_HTTPLIB2:
        module.fail_json(msg="httplib2 is not installed")

    endpoint = module.params['endpoint']
    state = module.params['state']
    model = module.params['model']
    apiVersion = 'v1'
    kind = None
    metadata = None
    h = httplib2.Http()

    if 'apiVersion' in model :
        apiVersion = model['apiVersion']

    if 'kind' in model :
        kind = K8S_TYPE.get(model['kind'].lower())
    else :
        module.fail_json(changed=False, msg='model.kind is a required property')

    if 'metadata' in model :
        metadata = model['metadata']
        if 'name' not in metadata :
            module.fail_json(changed=False, msg='model.metadata.name is a required property')

    else :
        module.fail_json(changed=False, msg='model.metadata is a required property')

    response, content = h.request(endpoint + '/api/' + apiVersion +
            '/' + kind + '/' + metadata['name'])

    if response.status == 404:

        if 'present' == state.lower() :
            module.fail_json(changed=False, msg='Create is not supported for ' + kind + ' ' + content)

    else:

        if 'absent' == state.lower() :

            response, content = h.request(endpoint + '/api/' + apiVersion +
                '/' + kind + '/' + metadata['name'],
                    method='DELETE')

            if response.status >= 400:
                module.fail_json(changed=False, msg='Failed to delete ' + kind)
            else:
                module.exit_json(changed=True, content=content)

        if 'present' == state.lower() :
                
            json_resp = json.loads(content)
            
            if 'spec' in model:
                json_resp['spec'].update(model['spec'])
            if 'status' in model:
                json_resp['status'].update(model['status'])
                
            response, content = h.request(endpoint + '/api/' + apiVersion +
                '/' + kind + '/' + metadata['name'], method='PUT', 
                headers={'Content-Type':'application/json'}, body=json.dumps(json_resp))

            if response.status >= 400:
                module.fail_json(changed=False, msg='Failed to update ' + kind + ' ' + content)
            else:
                module.exit_json(changed=True, content=content)

        else:

            module.exit_json(changed=False, content=content)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
