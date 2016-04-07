#!/usr/bin/python

HAS_HTTPLIB2 = True
try:
    import httplib2
except ImportError:
    HAS_HTTPLIB2 = False

import json

K8S_TYPE = {
    'pod' : 'pods',
    'replicationcontroller' : 'replicationcontrollers',
    'service' : 'services',
    'endpoints' : 'endpoints'
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
        if 'namespace' not in metadata :
            module['namespace'] = 'default'
    else :
        module.fail_json(changed=False, msg='model.metadata is a required property')

    response, content = h.request(endpoint + '/api/' + apiVersion +
            '/namespaces/' + metadata['namespace'] +
                '/' + kind + '/' + metadata['name'])

    if response.status == 404:

        if 'present' == state.lower() :

            response, content = h.request(endpoint + '/api/' + apiVersion +
                '/namespaces/' + metadata['namespace'] + '/' + kind,
                    method='POST', headers={'Content-Type':'application/json'}, body=json.dumps(model))

            if response.status >= 400:
                module.fail_json(changed=False, msg='Failed to create ' + kind + ' ' + content)
            else:
                module.exit_json(changed=True, content=content)

        else:

            module.exit_json(changed=False, content=content)

    else:

        if 'absent' == state.lower() :

            response, content = h.request(endpoint + '/api/' + apiVersion +
                '/namespaces/' + metadata['namespace'] + '/' + kind + '/' + metadata['name'],
                    method='DELETE')

            if response.status >= 400:
                module.fail_json(changed=False, msg='Failed to delete ' + kind)
            else:
                module.exit_json(changed=True, content=content)

        if 'present' == state.lower() and kind != 'services' :

            response, content = h.request(endpoint + '/api/' + apiVersion +
                '/namespaces/' + metadata['namespace'] + '/' + kind + '/' + metadata['name'],
                    method='PUT', headers={'Content-Type':'application/json'}, body=json.dumps(model))

            if response.status >= 400:
                module.fail_json(changed=False, msg='Failed to update ' + kind)
            else:
                module.exit_json(changed=True, content=content)

        else:

            module.exit_json(changed=False, content=content)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
