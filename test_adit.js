import http from 'k6/http';
import { check, sleep } from 'k6';

const baseUrl = 'https://reqres.in';

export default function () {
    let payloadCreate = {
        name: 'morpheus',
        job: 'leader',
    };
    let headers = {
        'Content-Type': 'application/json',
    };
    let responseCreate = http.post(`${baseUrl}/api/users`, JSON.stringify(payloadCreate), { headers: headers });
    check(responseCreate, {
        'API Create - status is 201': (r) => r.status === 201,
    });

    let payloadUpdate = {
        name: 'morpheus',
        job: 'zion resident',
    };
    let responseUpdate = http.put(`${baseUrl}/api/users2`, JSON.stringify(payloadUpdate), { headers: headers });
    check(responseUpdate, {
        'API Update - status is 200': (r) => r.status === 200,
    });

    sleep(1);
}
